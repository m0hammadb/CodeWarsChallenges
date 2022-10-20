def scramble(s1, s2):
    myDict = {}
    for c in s1:
        if(c in myDict):
            myDict[c] += 1
        else:
            myDict[c] = 1

    for c in s2:
        if(c not in myDict or myDict[c] == 0):
            return False
        else:
            myDict[c] -= 1
    return True
