tuple1 = ([12,123,14],[332,66,77,8000],[10,(2000,3000,4000),20],[18,19,20])

lst = []
for ls in tuple1:
    currentLst = []
    for item2 in ls:
        
        if(type(item2) == tuple):
            tupleLst = []
            for tupleItem in item2:
                if(tupleItem != 2000):
                    tupleLst.append(tupleItem)
                else:
                    tupleLst.append(6000)
            currentLst.append(tuple(tupleLst))
        else:
            currentLst.append(item2)
    lst.append(currentLst)

finalTuple = tuple(lst)

print(finalTuple)