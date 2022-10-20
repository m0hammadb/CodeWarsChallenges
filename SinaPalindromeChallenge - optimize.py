largestFound = -1
largestI=-1
largestJ = -1
# oDictionary = {}
for i in range(100,1000):
    for j in range(100,1000):
        # key1 = "{}x{}".format(i,j)
        # key2 = "{}x{}".format(j,i)

        # if((key1 in oDictionary)):
        #     continue
        # if(key2 in oDictionary):
        #     continue
        # else:
        #     oDictionary[key1] = True
        #     oDictionary[key2] = True
        
        currentNumber = i * j

        t = currentNumber
        reversedNum=0
        while t > 0:

            reversedNum *= 10
            
            reversedNum += t % 10
            t = t // 10
        
        if(reversedNum == currentNumber and currentNumber > largestFound):
            largestFound = currentNumber
            largestI = i
            largestJ = j

print("{} x {}".format(largestI,largestJ))
print(largestFound)