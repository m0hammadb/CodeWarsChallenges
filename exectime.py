import time
def init_list():
    lst = [] 
    for i in range(0,5000000):
        lst.append(i)

    return lst 


start_time = time.time()
myList = init_list()
length = len(myList)
while(length > 0):
    myList.pop(-1)
print("--- %s seconds ---" % (time.time() - start_time))