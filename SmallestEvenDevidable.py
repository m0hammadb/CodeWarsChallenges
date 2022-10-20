stepper = 1

loggerDictionary = {}

firstNum = -1
n = 15
while True:

    for i in range(1,n + 1):
        current = i * stepper
        if(current in loggerDictionary):
            loggerDictionary[current] += 1
            if(loggerDictionary[current] >= n):
                firstNum = current
                break
        else:
            loggerDictionary[current] = 1
    if(firstNum > - 1):
        break
    stepper += 1

