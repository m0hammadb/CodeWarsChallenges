def longest_consec(strarr, k):
    if(k <= 0):
        return ""
    minMax = -1
    minMaxStr = ""
    longests = []
    for i in range(len(strarr)-k+1):
        currentString = ""
        for j in range(k):
            currentString += strarr[i+j]
        if(len(currentString) >= minMax):
            minMax = len(currentString)
            minMaxStr = currentString
            longests.append(minMaxStr)
    
    for i in range(len(longests)):
        for j in range(i+1,len(longests)):
            if(len(longests[i]) >= len(longests[j])):
                longests[i],longests[j] = longests[j],longests[i]
    
    if(not longests):
        return ""
    return longests[-1]

print(longest_consec( ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"],3))