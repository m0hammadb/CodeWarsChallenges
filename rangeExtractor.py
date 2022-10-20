def solution(numbers):
    ranges = ""
    pointer = 0
    length = len(numbers)
    lastNum = 0
    rangeList = []
    newRange = []
    while True:
        currentNum = numbers[pointer]
        if(not newRange):
            newRange.append(currentNum)

        else:
            if(abs(lastNum - currentNum) == 1):
                newRange.append(currentNum)
            else:
                rangeList.append(newRange)
                newRange = []
                newRange.append(currentNum)

        lastNum = currentNum
        pointer += 1
        if(pointer == length):
            break
    if(newRange):
        rangeList.append(newRange)

    for rng in rangeList:
        if(len(rng) > 2):
            ranges += str(rng[0]) + "-" + str(rng[-1]) + ","
        else:
             if(len(rng) == 2):
                 ranges += str(rng[0]) + "," + str(rng[1]) + ","
             else:
                 ranges += str(rng[0]) + ","

    return ranges[:-1]


print(solution([1,2,3,4,5,6,7,8,9]))
print(solution([-3,-2,-1,1,2,4,5,7,8,9]))