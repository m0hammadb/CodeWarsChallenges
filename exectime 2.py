import time
from random import randint
def init_list():
    lst = [] 
    for i in range(0,500000):
        newRandom = randint(1,10000)
        lst.append(newRandom)

    return lst 


start_time = time.time()
myList1 = init_list()
myList2 = init_list()

myDict = {}

distinct = []

for item in myList2:
    myDict[item] = 1

for item in myList1:
    if(item not in myDict):
        distinct.append(item)

print(len(distinct))
print("--- %s seconds ---" % (time.time() - start_time))