def move_zeros(lst):
    finalList = []
    zeroCount = 0
    for item in lst:
        if(item == 0):
            zeroCount += 1
        else:
            finalList.append(item)
    
    for i in range(zeroCount):
        finalList.append(0)
    
    return finalList