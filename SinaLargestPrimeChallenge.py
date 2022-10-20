import math 

inputNum = 6008514751

n = int(math.sqrt(inputNum))

numbersList=[]
i = 0
while(i <= n):
    numbersList.append(1)
    i += 1

starter = 2
while True:
    if(numbersList[starter] == 1):
        i=2
        while (starter * i) <= n:
            numbersList[starter * i] = -1
            i += 1

    starter += 1
    if(starter * 2 > n):
        break

for i in range(2,n):
    if(numbersList[i] != -1):
        if(inputNum % i == 0):
            print(i)