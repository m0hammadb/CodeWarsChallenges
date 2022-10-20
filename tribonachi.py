def tribonacci(signature, n):
    final = []
    final.extend(signature)
    if(n <= 3):
        return signature[:n]
    for i in range(2,n-1):
        newNum = final[i] + final[i-1] + final[i-2]
        final.append(newNum)
    return final

print(tribonacci([1,1,1], 10))