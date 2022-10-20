largestFound = -1
for i in range(100,1000):
    for j in range(100,1000):

        currentNumber = i * j

        t = currentNumber
        reversedNum=0
        while t > 0:

            reversedNum *= 10
            
            reversedNum += t % 10
            t = t // 10
        
        if(reversedNum == currentNumber):
            largestFound = currentNumber

print(largestFound)