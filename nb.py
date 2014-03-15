import sys
import numpy as np
import time
__author__ = 'khabbabs'

# files are parsed in the order to vocabulary train.label train.data test.label test.data

vocab = []
trainLabel = []
trainData = []
mapMatrix = np.zeros((20,61188))
probXGivenY = np.zeros((20,61188))


testLabel = []
testData = []

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
            # print(line.replace('\n',''))
            # print(line.split(' '))
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
        # goes through train.data
        # calculates how many times
        # a word appears in all docs
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
        print "START YOUR ENGINES"

        for c in range(20):
            for index,word in enumerate(vocab):

                top = mapMatrix[c][index] + alpha
                bot = totalWordsInEachClass[c] + (alpha * vocabLen)
                probXGivenY[c,index] = top / bot

        print "LIL ELEPHANT PEW PEW PEW"
#####################################################################


# ===================== MLE ========================================
        totalDocs = float(len(trainLabel))
        probClass = [ i/totalDocs for i in totalEachClass]

# ===================================================================








        tend = time.time()

        print "traning Complete: "+str((tend - tstart))


        # print(trainData)
        # totalWordCount = [0]*(len(vocab)+1)
        # for i in range(len(trainData)):
        #     tempWord = int(trainData[i][1])
        #     totalWordCount[tempWord]+=int(trainData[i][2])

        # print(totalWordCount)





if __name__ == '__main__':
    fileInput()