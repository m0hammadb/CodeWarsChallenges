def find_even_index(arr):
    totalSum = sum(arr)
    leftSum = 0
    rightSum = totalSum
    counter = 0
    for item in arr:
        if(leftSum == (totalSum - (item + leftSum))):
            
            return counter
        leftSum += item
        counter += 1
    return -1

print(find_even_index(list(range(-100,-1))))