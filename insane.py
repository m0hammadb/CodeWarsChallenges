import math
baseDict = {}
combDict = {}
def toBase3(inp):
    if(inp in baseDict):
        return baseDict[inp]
    final = {}
    backupi = inp
    if(inp == 0):
        return {0:0,"s":1}
    counter = 0
    while inp > 0:
        final[counter] = inp % 3
        counter += 1 
        inp = inp // 3
    final["s"] = counter
    baseDict[backupi] = final
    return final

def fastComb3(n,m):
    if(m > n):
        return 0
    else:
        if(n==0 or n==1):
            return 1
        elif(n==2):
            if(m == 1):
                return 2
            else:
                return 1

def fastBase3Comb(n,m):
    

    nList = toBase3(n)
    mList = toBase3(m)
    prod = 1
    k = nList["s"]
    c = mList["s"]
    for i in range(k):
        currentN = nList[i]
        currentM = 0
        if(i < c):
            currentM = mList[i]
        comb = fastComb3(currentN,currentM)
        comb = comb % 3
        prod *= comb 
    result = prod % 3
    return result
    
def charToInt(char):
    if(char == "R"):
        return 0
    elif(char == "G"):
        return 1
    elif(char == "B"):
        return 2
    else:
        return -1

def intToChar(inp):
    if(inp == 0):
        return "R"
    elif(inp == 1):
        return "G"
    elif(inp == 2):
        return "B"
def triangle(m):    
    tSum = 0
    length = len(m)
    lengthbase3 = toBase3(length-1)
    for i in range(0,length):
        current = m[i]
        cCode = charToInt(current)
        #combin = math.comb(length-1,i)

        combin2 = fastBase3Comb(length-1,i)
        #combin2 = 1
        #combin = combin % 3
        tSum += (combin2 * cCode)

    po = ((length % 2) * 2 - 1) % 3
    tSum = (po * tSum) % 3
    return intToChar(tSum)
#a = "RGRRGBRGB"
triangle("RG")

