def is_ascending(numbers):
    length = len(numbers)
    for i in range(length - 1):
        if(i < length - 1):
            if(numbers[i] > numbers[i + 1]):
                return False 
    return True

print(is_ascending([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]))