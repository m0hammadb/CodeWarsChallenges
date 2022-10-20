def rot13(message):
    alphas = "abcdefghijklmnopqrstuvwxyz"
    maxLength = len(alphas)
    charDict = {}
    numDict = {}
    final = ""
    for i in range(maxLength):
        charDict[alphas[i]] = i
        numDict[i] = alphas[i]
    
    for c in message:
        lowerC = c.lower()
        if(lowerC not in charDict):
            final += c
        else:
            
            currentPosition = charDict[lowerC]
            correctLetter = ""
            if(currentPosition + 13 < maxLength):
                correctLetter = numDict[currentPosition + 13]
            else:
                correctLetter = numDict[(currentPosition - 26) + 13]
            if(c != lowerC):
                correctLetter = correctLetter.upper()
            final += correctLetter
    
    return final

def rot13_second(message):
    alphas = "abcdefghijklmnopqrstuvwxyz"
    convertDict = {}
    final = ""
    for i in range(len(alphas)):
        current = alphas[i]
        j = -1
        
        if(i + 13 < len(alphas)):
            j = i + 13
        else:
            j = i - 26 + 13
            
        convertDict[current] = alphas[j]
        convertDict[current.upper()] = alphas[j].upper()

    for c in message:
        if(c in convertDict):
            final += convertDict[c]
        else:
            final += c 
    
    return final
    

print(rot13_second("TestA#abs"))
print(rot13("TestA#abs"))