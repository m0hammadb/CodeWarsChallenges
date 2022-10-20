def findMissing(numbers):
    maxRange = len(numbers)-1
    originalSum = sum(x for x in range(0,maxRange+1))
    newSum = sum(numbers)
    return newSum - originalSum


print(findMissing([3,1,3,4,2]))