def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    rList = []
    for i in range(a,b+1):
        p = 1
        sum = 0
        for c in str(i):
            sum += int(c) ** p
            p += 1
        if(sum == i):
            rList.append(i)
    return rList