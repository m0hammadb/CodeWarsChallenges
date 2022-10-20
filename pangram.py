def is_pangram(s):
    myDict = {}
    s = s.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for a in alpha:
        myDict[a] = 1
        count += 1
    for char in s:
        if(char in myDict):
            myDict.pop(char)
            count -= 1
    return count == 0

print(is_pangram("The quick brown fox jumps over the lazy dog"))