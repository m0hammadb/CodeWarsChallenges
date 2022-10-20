def getNumKey(key):
    sortedKey = list(key)
    sortedKey.sort()
    finalResult = ""
    for s in key:
        finalResult += str(sortedKey.index(s)) + ","
    
    rValue = [int(x) for x in finalResult[:-1].split(",")]
    return rValue

def getDecodeKey(length):
    key = ""
    rList = []
    for i in range(0,length):
        rList.append(i)
    return rList


def createDictionary(value,numericKey):
    myDict = {}

    for digit in numericKey:
        myDict[digit] = []
    i = 0
    j = 0
    length = len(value)
    dicLength = len(numericKey)
    while True:
        if(i < length ):
            myDict[numericKey[j]].append(value[i])

            j += 1
            if(j == dicLength):
                j = 0
            i += 1
        else:
            break
    
    return myDict


def getValueFromDictionary(myDict,numericKey,maxLength):
    maxKey = max(numericKey)
    currentLength = 0
    final = ""
    dicIndex = 0
    while currentLength < maxLength:
        for i in range(0,int(maxKey)+1):
            try:
                final += myDict[i][dicIndex]
            except:
                final += " "
                #myDict[str(i)].pop(0)
            currentLength += 1
        dicIndex += 1
    return final

def getDecodeValueFromDictionary(myDict,numericKey,maxLength):
    maxKey = max(numericKey)
    currentLength = 0
    final = ""
    while currentLength < maxLength:
        for i in numericKey:
            if(myDict[i]):
                final += myDict[i][0]
                myDict[i].pop(0)
                currentLength += 1
    return final
def nico(key,message):
    numKey = getNumKey(key)
    myDict = createDictionary(message, numKey)
    finalValue = getValueFromDictionary(myDict, numKey, len(message))
    return finalValue

def de_nico(key,message):
    decodeKey = getDecodeKey(len(key))
    normalKey = getNumKey(key)
    myDict = createDictionary(message,decodeKey)
    finalValue = getDecodeValueFromDictionary(myDict, normalKey, len(message))
    return finalValue.strip()

key = "crazy"
message = "secretinformation"
eNico = nico(key, message)
print(eNico)
dNico = de_nico(key,eNico)
print(dNico)
