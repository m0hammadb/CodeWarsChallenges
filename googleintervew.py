blocks = [
    {
        "gym":False,
        "school": True,
        "store": False
    },
    {
        "gym":False,
        "school": False,
        "store": False
    },
    {
        "gym":True,
        "school": True,
        "store": False
    },
    {
        "gym":False,
        "school": True,
        "store": False
    },
    {
        "gym":False,
        "school": False,
        "store": True
    }
]

reqs = ["gym","school","store"]

blockCosts = []
allReqs = []
for req in reqs:
    reqList = []
    for dic in blocks:
        if(dic[req] == True):
            reqList.append(1)
        else:
            reqList.append(0)
    allReqs.append(reqList)

allCosts = []

for req in allReqs:
    costList = []
    for i in range(len(req)):
        block = req[i]
        if(block == 1):
            costList.append(0)
        else:
            currentCost = 0
            rightCost = -1
            leftCost = -1
            for j in range(i+1,len(req)):
                currentCost += 1
                if(req[j] == 1):
                    rightCost = currentCost
                    break
            currentCost = 0
            for j in range(i-1,-1,-1):
                currentCost += 1
                if(req[j] == 1):
                    leftCost = currentCost
                    break
            finalCost = -1
            if(leftCost != -1 and rightCost != -1):
                finalCost = min(leftCost,rightCost)
            elif(leftCost == -1):
                finalCost = rightCost
            else:
                finalCost = leftCost
            costList.append(finalCost)
    allCosts.append(costList)
                    

finalSum = []
maxValues = []
for i in range(len(blocks)):
    costSum = 0
    maxValue = 0
    for j in range(len(allCosts)):
        costSum += allCosts[j][i]
        if(allCosts[j][i] > maxValue):
            maxValue = allCosts[j][i]
    maxValues.append(maxValue) 
    finalSum.append(costSum)

print(finalSum)
print(maxValues)