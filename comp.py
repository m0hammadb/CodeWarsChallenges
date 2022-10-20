import math
def comp(array1, array2):
    firstDict = {}
    for item in array1:
        if(item not in firstDict):
            firstDict[item] = 1
        else:
            firstDict[item] += 1

    for item in array2:
        compar = math.sqrt(item)
        if(compar in firstDict):
            firstDict[compar] -= 1
            if(firstDict[compar] <= 0):
                firstDict.pop(compar)
        else:
            return False
    
    return True

print(comp([121, 144, 19, 161, 19, 144, 19, 11],[11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
	