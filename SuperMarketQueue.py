customers = [10,2,3,3]
tillCount = 2

tills = []
for i in range(tillCount):
    tills.append(0)

totalTime = 0


while True:
    
    zeroCount = 0
    for i in range(tillCount):
        if(tills[i] != 0):
           tills[i] -= 1

        if(tills[i] == 0):
             if(len(customers) > 0):
                currentCustomer = customers[0]
                customers.pop(0)
                tills[i] = currentCustomer
             else:
                zeroCount += 1

    if(zeroCount == tillCount):
        break

    totalTime += 1

print(totalTime)