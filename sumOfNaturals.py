def sumOfNaturals(n):
    if(n == 0):
        return 0
    return n + sumOfNaturals(n-1)

print(sumOfNaturals(10))