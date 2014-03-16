import sys
import numpy as np
import time
import math
__author__ = 'khabbabs'

# files are parsed in the order to vocabulary train.label train.data test.label test.data




vocab = []
trainLabel = []
trainData = []
mapMatrix = np.zeros((20,61188))
probXGivenY = np.zeros((20,61188))
#makes confusion matrix for classifiers
confMatrix=np.zeros((20,20))


testLabel = []
testData = []

# to run file python nb.py vocabulary.txt train.label train.data test.label test.data

def fileInput():

    print "stated parsing"
    # parsing vocabulary.txt
    with open(sys.argv[1]) as f:
        for index, line in enumerate(f):
            vocab.append(line.strip())

    totalEachClass = [0] * 20

    with open(sys.argv[2]) as f:
        for index, line in enumerate(f):
            trainLabel.append(line.strip())
            totalEachClass[int(line)-1]+=1



    with open(sys.argv[3]) as f:
        for line in f:
            line = line.strip()
            newline = line.split(' ')
            trainData.append(newline)

    with open(sys.argv[4]) as f:
        for index, line in enumerate(f):
            testLabel.append(line.strip())

    with open(sys.argv[5]) as f:
        for line in f:
            line = line.strip()
            newline = line.split(' ')
            testData.append(newline)


        print "ended parsing"



# =====================MAP SECTION===================================

 # Goes through train.data  calculates how many times a word appears
 # in all docs. mapMatrix is 20 by 61188 matrix which holds the total
 # word count corresponding to the classifer and the word. This gets
 # used when we need to calculate P(x|y). (check formulas)
 #
 # totalWordsInEachClass counts total words in all the classes.
 #

        tstart = time.time()
        vocabLen = float(len(vocab))
        alpha = 1 / vocabLen
        dirichlet = 1.0 + alpha
        totalWordCount = [0]*(len(vocab)+1)
        # print type(sparseMatrix[0][1])
        for index,line in enumerate(trainData):
            line.append(str(trainLabel[int(line[0])-1]))
            totalWordCount[int(line[1])]+=int(line[2])
            mapMatrix[int(line[3])-1][int(line[1])-1]+=int(line[2])


        totalWordsInEachClass = [sum(mapMatrix[x]) for x in range(20)]
        

# ======================= calculating prob(X | Y) ==================
# '''
#  This section is calculating the probabilty of each word given a classifier.
#  formula:
#                                   (count of Xi in Yk) + a
#        P(Xi|Yk)  = ------------------------------------------------------
#                     (total words in Yk) + ( a * (lenght of vocab list))
#
# '''

        print "Calculation prob(x | y )"
        for c in range(20):
            for index,word in enumerate(vocab):

                top = mapMatrix[c][index] + alpha
                bot = totalWordsInEachClass[c] + (alpha * vocabLen)
                probXGivenY[c,index] = float(top) / float(bot)

#####################################################################


# ===================== MLE ========================================
# '''
#  calculating MLE
#
#               # of docs labeled yk
#  P(Yk) = ---------------------------------
#                tatal # of docs
#
# '''


        totalDocs = float(len(trainLabel))
        probClass = [ i/totalDocs for i in totalEachClass]

# ===================================================================
# '''
#    this section is classifying the test data.
#
#    formula:          Ynew = argmax (log(P(Yk)) + sum(# of word xnew in test.data )*log(P(xnew|Yk)))
#
#
# '''
        tend = time.time()

        print "traning Complete: "+str((tend - tstart))


        print "Test start"

        tempArray = []
        docCheck = int(testData[0][0])
        classArray = []
        checkClass = []

        for elemment in testData:

            if int(elemment[0]) == docCheck:
                tempArray.append(elemment[1:])

            else:
               
                for sub in range(20):
                    classLog = math.log(probClass[sub])
                    countWord = sum([ (float(i[1])) * (math.log(probXGivenY[sub,int(i[0])-1])) for i in tempArray])
                    classArray.append(classLog+countWord)

    
                checkClass.append(classArray.index(max(v for v in classArray))+1)
                docCheck = int(elemment[0])
                tempArray = []
                classArray= []


        print "total words in test.data: "+ str((len(checkClass)))
        print "matched correctly:        "+str(len([i for i in range(len(checkClass)) if int(checkClass[i])==int(testLabel[i])]))

#==============================builds confusion matrix==================================

        
        print "start confusion matrix"
        for i in range(len(checkClass)):
            if int(checkClass[i])==int(testLabel[i]):
                confMatrix[int(checkClass[i])-1][int(testLabel[i])-1]+=1
            else:
                confMatrix[int(checkClass[i])-1][int(testLabel[i])-1]+=1
        np.set_printoptions(precision=1,linewidth=150)
        print confMatrix
        print "Confusion Matrix printed"





        print "Test End"

if __name__ == '__main__':
    fileInput()
