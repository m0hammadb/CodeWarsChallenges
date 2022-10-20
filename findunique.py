def find_uniq(arr):
    #Find the norm

    norm = 0
    if(arr[0] == arr[1]):
        norm = arr[0]
    else:
        if(arr[1] == arr[2]):
            return arr[0]
        else:
            return arr[1]
    for i in range(2,len(arr)):
        if(arr[i] != norm):
            return arr[i]
       # n: unique number in the array