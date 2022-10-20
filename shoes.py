def pair_of_shoes(shoes):
    shoeDict = {}
    count = 0
    for item in shoes:
        ty = item[0]
        size = item[1]
        if(ty == 0):
            ty = -1
        
        if(size in shoeDict):
            shoeDict[size] += ty 
            if(shoeDict[size] == 0):
                shoeDict.pop(size)
                count -= 1
        else:
            shoeDict[size] = ty
            count += 1

    return count == 0

print(pair_of_shoes([[0, 21], [1, 23], [1, 21], [0, 23]]))