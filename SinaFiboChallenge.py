fiboList=[1,2]
lastIndex=1

fiboSum = 2
while True:

    newFibo = fiboList[lastIndex] + fiboList[lastIndex - 1] 
    lastIndex += 1
    fiboList.append(newFibo)
    if(newFibo % 2 == 0):
        fiboSum += newFibo

    if(newFibo > 4000000):
        break

print("Sum of even fibos: ",fiboSum)