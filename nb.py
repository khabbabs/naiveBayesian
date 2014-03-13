import sys


__author__ = 'khabbabs'

# files are parsed in the order to vocabulary train.label train.data

vocab = dict()
trainLabel = dict()
trainData = []
def fileInput():


    # parsing vocabulary.txt
    with open(sys.argv[1]) as f:
        for index, line in enumerate(f):
            vocab.__setitem__(index,line.replace('\n',''))


    with open(sys.argv[2]) as f:
        for index, line in enumerate(f):
            trainLabel.__setitem__(index,line.replace('\n',''))



    with open(sys.argv[3]) as f:
        for line in f:
            # print(line.replace('\n',''))
            # print(line.split(' '))
            line = line.strip()
            newline = line.split(' ')
            trainData.append(newline)




        for index,line in enumerate(vocab):
            print(sum([int(x[2]) for x in trainData if x[1] == str(index) ]))

        # print(trainData)
        # totalWordCount = [0]*(len(vocab)+1)
        # for i in range(len(trainData)):
        #     tempWord = int(trainData[i][1])
        #     totalWordCount[tempWord]+=int(trainData[i][2])

        # print(totalWordCount)





if __name__ == '__main__':
    fileInput()