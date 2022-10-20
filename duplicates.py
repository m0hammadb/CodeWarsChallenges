def dup_number(inp):
    myDict = {}
    count = 0
    for character in inp:
        character = str(character).lower()
        if(character in myDict):
            myDict[character] += 1
            if(myDict[character] == 2):
                count += 1
        else:
            myDict[character] = 1
    
    return count

inp = "abcdAbbC"
print(dup_number(inp))