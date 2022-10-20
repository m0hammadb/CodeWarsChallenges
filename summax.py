from sys import maxsize


def max_sumDig(nMax, maxSum):
    goodCount = 0
    totalSum = 0
    goodNums = []
    for i in range(1000,nMax + 1):
        nList = [int(x) for x in list(str(i))]
        goodNum = True
        for j in range(0,len(nList)):
            currentSum = sum(nList[j:j+4])
            if(currentSum > maxSum):
                goodNum = False
        
        if(goodNum):
            goodCount += 1
            totalSum += i 
            goodNums.append(i)
        
    average = totalSum // goodCount
    mindif = -1
    if(len(goodNums) > 0):
        nearest = goodNums[0]
        mindif
        for i in range(1,len(goodNums)):
            if(abs(goodNums[i] - average) <= abs(nearest - average)):
                
                nearest = goodNums[i]
    
    return [goodCount,nearest,totalSum]

max_sumDig(5000,6)