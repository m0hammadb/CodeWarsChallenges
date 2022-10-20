n = 4673473

temp = n

rev=0
while temp > 0:
    rev *= 10
    lastDigit=temp % 10
    temp = temp // 10
    rev += lastDigit

print(rev)