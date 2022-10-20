def min_value_index(lst):

    if(len(lst) == 0):
        return None
    
    minValue = lst[0]
    minIndex = 0
    for v in range(len(lst)):
        if(lst[v] < minValue):
            minValue = lst[v]
            minIndex = v

    return minIndex

def least_larget(lst,pIndex):

    if(pIndex >= len(lst)):
        return -1

    biggerList=[]
    indexList =[]
    for i in range(len(lst)):
        if(lst[i] > lst[pIndex]):
            biggerList.append(lst[i])
            indexList.append(i)
    
    minIndex = min_value_index(biggerList)
    if(minIndex != None):
        return indexList[minIndex]

    return -1


lst = [3,2,7,1,8,9,6,0,-2]
leastIndex = least_larget(lst, 6)
print(leastIndex)