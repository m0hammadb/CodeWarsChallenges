def largest_sum(arr):
    highestSum = 0
    currentSum = 0
    myList = []
    for item in arr:
        if(item < 0):
            highestSum = currentSum
            myList.append(highestSum)
            myList.append(item)
            currentSum = 0
        else:
            currentSum += item
    if(currentSum != 0):
        myList.append(currentSum)
    
    highestSum = 0
    myLength = len(myList)
    for i in range(myLength):
        for j in range(i,myLength):
            cSum = sum(myList[i:j+1])
            if(cSum > highestSum):
                highestSum = cSum
    return highestSum

print(sum([31,-41,59,26,-53,58,97,-93,-23,84]))
print(largest_sum([31,-41,59,26,-53,58,97,-93,-23,84]))
a = [1,3,4,5,7,2,-1,3,18,23,-2,180]