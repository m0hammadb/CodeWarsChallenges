def orderPlease(myLst):
    words = myLst.split(" ")
    myDict = {}
    biggestNum = -1
    final = ""
    for i in range(len(words)):
        word = words[i]
        num = getNumFromString(word)
        if(num > biggestNum):
            biggestNum = num
        myDict[num] = word

    for i in range(1,biggestNum + 1):
        final += myDict[i]
        if(i < biggestNum):
            final += " "
        
    return final

def getNumFromString(inp):
    nums = "0123456789"
    for c in inp:
        if(c in nums):
            return int(c)


orderPlease("4of Fo1r pe6ople g3ood th5e the2")