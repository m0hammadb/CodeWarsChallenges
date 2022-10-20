def next_smaller(n):
    strNumber = str(n)
    length = len(strNumber)
    pointer = length - 1
    while True:
        cCount = 0
        cList = []
        for i in range(pointer,length):
            a = strNumber[i]
            cList.append(a)
            cCount += 1
        checking = cList[0]
        smallerList = []
        for i in range(1,cCount):
            if(cList[i] < checking):
                smallerList.append(cList[i])

        if(pointer == 0):
                if(0 in smallerList):
                    smallerList.remove(0)
        if(len(smallerList) > 0):
            
            
            remains = strNumber[0:pointer]
            assignNumber = max(smallerList)
            cList.remove(assignNumber)
            cList.sort(reverse=True)
            cList.insert(0, assignNumber)
            final = int(remains + "".join([x for x in cList]))
            if(len(str(final)) == len(strNumber)):
                return final
            
        pointer -= 1
        if(pointer == -1):
            return -1


print(next_smaller(1234567908))