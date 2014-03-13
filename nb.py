import sys


__author__ = 'khabbabs'

# files are parsed in the order to vocabulary train.label train.data

vocab = []
trainLabel = []
trainData = []
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
        vocabLen = len(vocab)
        sparseMatrix = [[0 for i in range(vocabLen+1) ] for j in range(20)]
        totalWordCount = [0]*(len(vocab)+1)
        # print type(sparseMatrix[0][1])
        for index,line in enumerate(trainData):
            line.append(str(trainLabel[int(line[0])-1]))
            totalWordCount[int(line[1])]+=int(line[2])
            sparseMatrix[int(totalWordCount[3])][int(totalWordCount[1])]+=int(totalWordCount[2])





        # print(vocab)
        # print(trainLabel)






# ==================================================================




        # print(trainData)
        # totalWordCount = [0]*(len(vocab)+1)
        # for i in range(len(trainData)):
        #     tempWord = int(trainData[i][1])
        #     totalWordCount[tempWord]+=int(trainData[i][2])

        # print(totalWordCount)





if __name__ == '__main__':
    fileInput()