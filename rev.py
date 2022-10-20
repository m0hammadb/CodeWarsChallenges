def revNum(num):

    final = 0
    while num > 0:
        final = final * 10
        final += num % 10
        num = num // 10

    return final 

print(revNum(1234))