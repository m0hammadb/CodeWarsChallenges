def calculate_queue(customers,n):
    if(not customers):
        return 0
    customers = customers[::-1]
    totalTime = 0
    while True:
        energy = n
        for i in range(len(customers) - 1,-1,-1):
            customers[i] -= 1
            if(customers[i] == 0):
                customers.pop(i)
            energy -= 1
            if(energy == 0):
                break
        
        totalTime += 1 
        if(isAllZeros(customers)):
            break    
        
    return totalTime

def isAllZeros(lst):
    for item in lst:
        if(item != 0):
            return False
    return True

print(calculate_queue([2,3,10,5,4],2))