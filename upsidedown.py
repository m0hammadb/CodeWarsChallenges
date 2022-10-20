


def isUpsideDown(number):
    upDict = {1:1,6:9,8:8,9:6,0:0}
    strNum = str(number)
    length = len(strNum)
    for i in range(length):
        if(int(strNum[i]) not in upDict):
            return False
        upsideValue = str(upDict[int(strNum[i])])
        if(strNum[length-i-1] != upsideValue):
            return False
    
    return True # if we get to this point no return False was entered so its true



def solve(a, b):
    lst = []
    for i in range(a,b+1):
        if(isUpsideDown(i)):
            lst.append(i)
    
    return len(lst)
print(solve(100,1000))
