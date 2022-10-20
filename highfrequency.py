def countWords(inp):
    inp = inp.lower()
    highest = ["","",""]
    highestCount = [0,0,0]
    currentWord=""
    myDict = {}
    for char in inp:
        if(char.isalpha() or char == "'"):
            currentWord += char
        else:
            if(not isValid(currentWord)):
                currentWord = ""
            if(len(currentWord) > 0):
                if(currentWord in myDict):
                    myDict[currentWord] += 1
                else:
                    
                    myDict[currentWord] = 1
                cCount = myDict[currentWord]
                currentIndex = -1
                if(currentWord in highest):
                    currentIndex = highest.index(currentWord)
                for i in range(3):
                    if(cCount > highestCount[i]):
                        if(currentIndex == -1 or i == currentIndex):
                            highestCount[i] = cCount
                        
                            highest[i] = currentWord
                        else:
                            highest[currentIndex],highest[i] = highest[i],highest[currentIndex]
                            highestCount[currentIndex],highestCount[i] = highestCount[i],highestCount[currentIndex]
                            highestCount[i] = cCount
                        break
                
            currentWord = ""
    if(not isValid(currentWord)):
                currentWord = ""
    if(currentWord != ""):
        if(currentWord in myDict):
            myDict[currentWord] += 1
        else:
            myDict[currentWord] = 1
        cCount = myDict[currentWord]
        currentIndex = -1
        if(currentWord in highest):
            currentIndex = highest.index(currentWord)
        for i in range(3):
            if(cCount > highestCount[i]):
                if(currentIndex == -1 or i == currentIndex):
                    highestCount[i] = cCount
                
                    highest[i] = currentWord
                else:
                    highest[currentIndex],highest[i] = highest[i],highest[currentIndex]
                    highestCount[currentIndex],highestCount[i] = highestCount[i],highestCount[currentIndex]
                    highestCount[i] = cCount
                break



    for i in range(len(highestCount)-1,-1,-1):
        if(highestCount[i] == 0 ):
            highest.pop(i)
    return highest

def isValid(inp):
    valid = False
    for c in inp:
        if(c.isalpha()):
            return True
    return False
print(countWords("'''"))