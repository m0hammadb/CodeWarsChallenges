import time
import random
def init_list():
    lst = [] 
    for i in range(0,50000):
        lst.append(random.randint(1,100000))

    return lst 
def sort_the_odd(numbers):
    myOddNumber = []
    result = []
    for number in numbers:
        if not number % 2 == 0:
            myOddNumber.append(number)
    odd = sorted(myOddNumber)
    
    index = 0   
    for num in numbers:
        if num % 2 == 0 :
            result.append(num)
        elif not num % 2 == 0 :
            result.append(odd[index])
            index += 1           
    return result
def sort_odd(array):
    #step 1: getting odds and their index
    oddList =[]
    indexList =[]
    for i in range(len(array)):
        if array[i] % 2 != 0:
            oddList.append(array[i])
            indexList.append(i)
    #step 2: sorting the odds
    for i in range(len(oddList)):
        for j in range(i+1, len(oddList)):
            if not oddList[i] < oddList[j]:
                oddList[i], oddList[j] = oddList[j], oddList[i]
    #step 3: return the sorted odds to the array according to their index
    for i in range(len(array)):
        for j in range(len(indexList)):
            if i == indexList[j]:
                array[i] = oddList[j]
    return array

def sort_array(source_array):
    for i in range(len(source_array)):
        if(source_array[i] % 2 != 0):
            for j in range(i,len(source_array)):
                if(source_array[j] % 2 != 0):
                    if(source_array[i] > source_array[j]):
                        source_array[i],source_array[j] = source_array[j],source_array[i]
    return source_array
lst = init_list()



start_time = time.time()
sort_odd(lst)
print("--- %s seconds ---" % (time.time() - start_time))