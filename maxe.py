from re import I


def delete_nth(order,max_e):
    myDict = {}
    returnList = []
    for item in order:
        if(item in myDict):
            myDict[item] += 1
        else:
            myDict[item] = 1

        if(myDict[item] <= max_e):
            returnList.append(item)
    
    
    return returnList

delete_nth([20,37,20,21],1)