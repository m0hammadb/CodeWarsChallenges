
# adbcdef dce
memoDict = {}
def lcsT(str1,str2,callers =""):
    #base case
    doReturn = True
    for c in str2:
        if(c in str1):
            doReturn = False
            break
    if(doReturn):
        return [callers]
    counter = 0
    allList = []
    longest = 0
    start = 0
    for char in str2:
        while True:
            firstOccur = str1.find(char,start)
            if(firstOccur == -1):
                start = 0
                break
            caller = char 
            remain = str1[firstOccur + 1:]
            result = []
            if(len(str2) > 0):
                if((str1,str2) not in memoDict):
                    result = lcsT(remain,str2[counter + 1:],callers + caller)
                    memoDict[(str1,str2)] = result
                else:
                    result = memoDict[(str1,str2)]
            if(result):
                allList.extend(result)
            start += 1
        
        counter += 1
    maxLen = 0
    rList = []
    return allList

def lcs(str1,str2):
    memoDict = {}
    allSubs = lcsT(str1, str2)
    maxLength=0
    maxItem = ""
    for item in allSubs:
        cLength = len(item)
        if(cLength > maxLength):
            maxLength = cLength
            maxItem = item
    return maxItem

a = "abcdefghijklmnopqashasgh"
b = "apcdefghijklmnobqasgasha"

c = lcs(a, b)

print(c)