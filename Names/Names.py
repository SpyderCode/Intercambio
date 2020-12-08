import os.path
import random
import time

def getNames():
    f = open(os.path.dirname(__file__) + "/../NamesAndEmails.txt", "r")
    nameList = []
    for line in f:
        line = line[:line.find(":")]
        nameList.append(line)

    f.close()
    return nameList

def getEmails():
    f = open(os.path.dirname(__file__) + "/../NamesAndEmails.txt", "r")
    emailList=[]

    for line in f:
        line = line[line.find(":")+1:-1]
        emailList.append(line)

    f.close()
    return emailList

def RandomizeDest(DestinationList):
    randomized_list = DestinationList[:]
    while True:
        random.shuffle(randomized_list)
        for a, b in zip(DestinationList, randomized_list):
            if a == b:
                break
        else:
            return randomized_list