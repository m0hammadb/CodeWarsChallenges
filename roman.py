def normalCalc(n):
    romanDict = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
    final = ""
    backup = n
    for key in romanDict:
        if(n < key):
            continue
        
        c = n // key
        n = n - (c * key)
        if(c <= 3):
            final += (c * romanDict[key])
        else:
            return revCalc(backup)
    return final

def revCalc(n):
    romanDict = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
    lastBig = -1
    final = ""
    for key in romanDict:
        if(key > n):
            lastBig = key
            continue
        diffr = lastBig - n
        final = normalCalc(diffr) + romanDict[lastBig]
        return final

def solution(n):
    if(n <= 0 or n > 3999):
        return "Can't Compute this number"
        
    digitCount = len(str(n))
    powr = digitCount - 1
    final = ""
    for c in str(n):
        current = int(c) * (10 ** powr)
        if(current>0):
            final += normalCalc(current)
        powr -= 1

    return final    
        

print(solution(4000))