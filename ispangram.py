def is_pangram(s):
    alphas = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    alphaCount = len(alphas)
    myDict = {}
    for c in alphas:
        myDict[c] = 1

    for c in s:
        if(c in myDict):
            myDict.pop(c)
            alphaCount -= 1
    
    if(alphaCount == 0):
        return True
    else:
        return False 

print(is_pangram("mohammad"))
print(is_pangram("the quick brown fox jumps over the lazy dog"))
print(is_pangram("abcdefgh  ..$## igjklmnopqrstTUvwx  .,.'8765453yzz"))