import sys
import numpy as np

__author__ = 'khabbabs'

# files are parsed in the order to vocabulary train.label train.data

vocab = []
trainLabel = []
trainData = []
mapMatrix = np.zeros((20,61188))
alpha = 0.0
def fileInput():

    
    # parsing vocabulary.txt
    with open(sys.argv[1]) as f:
        for index, line in enumerate(f):
            vocab.append(line.strip())


    with open(sys.argv[2]) as f:
        for index, line in enumerate(f):
            trainLabel.append(line.strip())



    with open(sys.argv[3]) as f:
        for line in f:
            # print(line.replace('\n',''))
            # print(line.split(' '))
            line = line.strip()
            newline = line.split(' ')
            trainData.append(newline)

# =====================MAP SECTION===================================
        # goes through train.data
        # calculates how many times
        # a word appears in all docs
        alpha = 1 / float(len(vocab))
        print alpha
        totalWordCount = [0]*(len(vocab)+1)
        # print type(sparseMatrix[0][1])
        for index,line in enumerate(trainData):
            line.append(str(trainLabel[int(line[0])-1]))
            totalWordCount[int(line[1])]+=int(line[2])
            mapMatrix[int(line[3])-1][int(line[1])-1]+=int(line[2])

# ==================================================================




        # print(trainData)
        # totalWordCount = [0]*(len(vocab)+1)
        # for i in range(len(trainData)):
        #     tempWord = int(trainData[i][1])
        #     totalWordCount[tempWord]+=int(trainData[i][2])

        # print(totalWordCount)





if __name__ == '__main__':
    fileInput()