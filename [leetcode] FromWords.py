# 'thehat' 
# with , example , science

def countConstruct(target,words):
    myTarget = list(target)
    counter = 0
    while len(myTarget) > 0:
        commons = maxCommon("".join(myTarget), words)[1]
        if(len(commons) > 0):
            counter += 1
            for c in commons:
                myTarget.remove(c)
        else:
            counter = -1
            break
    return counter

        

def maxCommon(target,words):
    myDict = {}
    maxLength = 0
    maxWord = ""
    maxCommons = []
    for word in words:
        commons = []
        currentLength = 0
        for char in word:
            if(char not in myDict):
                myDict[char] = 1
            else:
                myDict[char] += 1
        
        for char in target:
            if (char in myDict):
                currentLength += myDict[char]
                if(myDict[char] > 0):
                    commons.append(char)
                myDict[char] -= 1
                
        if(currentLength > maxLength):
            maxLength = currentLength
            maxWord  = word
            maxCommons.clear() 
            maxCommons.extend(commons)
        
        myDict.clear()
    return [maxWord,maxCommons]

print(countConstruct("basicbasic", ["notice","possible","apple"]))
