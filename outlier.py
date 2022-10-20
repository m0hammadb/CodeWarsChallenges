def find_outlier(integers):
    searchMode = 0
    for i in range(3):
        if(integers[i] % 2 == 0):
            searchMode += 1
        else:
            searchMode -= 1

    for item in integers:
        if(searchMode > 0 and item % 2 != 0):
            return item
        elif(searchMode < 0 and item % 2 == 0):
            return item
    return -1

print(find_outlier([1,9,3,5,7]))