n = int(input("Please enter the number: "))
temp = n
digitCount = len(str(n))
sum = 0

while temp > 0:
    lastDigit = temp % 10
    temp = temp // 10
    sum = sum + (lastDigit ** digitCount)

if(sum == n):
    print("Yes")
else:
    print("No")
