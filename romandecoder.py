def solution(roman):
    romanDic = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    dic = {}
    length = len(roman)
    skipNext = False
    sumx = 0
    for i in range(length):
        if(skipNext):
            skipNext = False
            continue
        if(i<length-1):
            current = romanDic[roman[i]]
            nxt = romanDic[roman[i+1]]
            if(current >= nxt):
                sumx += current
            else:
                sumx += (nxt - current)
                skipNext = True
        else:
            sumx += romanDic[roman[i]]
    
    return sumx

print(solution("MDCLXVI"))