def queue(queuers,pos):
    currentPointer = 0
    totalTime = 0
    queueLength = len(queuers)
    while True:
        if(queuers[currentPointer] > 0):
            queuers[currentPointer] -= 1
            totalTime += 1
            if(currentPointer == pos):
                if(queuers[pos] == 0):
                    return totalTime
        currentPointer += 1
        if(currentPointer == queueLength):
            currentPointer = 0

