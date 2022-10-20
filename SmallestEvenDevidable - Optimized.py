def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

def findPrimesLessThanN(n):
    primes=[]
    for i in range(2,n):
        if(isPrime(i)):
            primes.append(i)

    return primes

def getPrimeMultipliersOfN(n):
    primes = findPrimesLessThanN(n)
    t = n
    returnList=[]
    if(isPrime(n)):
        return [n]
    while True:
        for num in primes:
            if(t % num == 0):
                returnList.append(num)
                t = t // num
                break
        if(t == 1):
            break
    return returnList

def countNum(lst,num):
    counter = 0
    for item in lst:
        if item == num:
            counter += 1
    return counter

n = 700
maxRepeatList=[]

for i in range(n+1):
    maxRepeatList.append(0)

for i in range(2,n+1):
    primeMultipliers = getPrimeMultipliersOfN(i)
    for item in primeMultipliers:
        itemCount = countNum(primeMultipliers, item)
        if(maxRepeatList[item] < itemCount):
            maxRepeatList[item] = itemCount

finalAnswer = 1
for i in range(len(maxRepeatList)):
    item = maxRepeatList[i]
    finalAnswer *= (i ** item)

print(finalAnswer)

