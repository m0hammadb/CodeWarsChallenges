def duplicate_encode(word):
    dupDict = {}
    word = word.lower()
    for item in word:
        if(item not in dupDict):
            dupDict[item] = 1
        else:
            dupDict[item] += 1
    final = ""
    for item in word:
        if(dupDict[item] == 1):
            final += "("
        else:
            final += ")"
    return final