def hamster_me(code, message):
    alphas = "abcdefghijklmnopqrstuvwxyz"
    sortedAlpha = list(code)
    sortedAlpha.sort()
    final = ""
    firstLetter = sortedAlpha[0]
    firstIndex = alphas.find(firstLetter)
    if(firstIndex > 0):
        alphas = alphas[firstIndex:] + alphas[0:firstIndex]
    encodeDict = {}
    for c in sortedAlpha:
        if(c not in encodeDict):
            encodeDict[c] = c + "1"
    
    header = ""
    counter = 1
    for c in alphas:
        if(c in encodeDict):
            header = c
            counter = 1
        else:
            counter += 1
            encodeDict[c] = header + str(counter)

    for c in message:
        final += encodeDict[c]
    return final
    

hamster_me("hhhhammmstteree","hamster")