def narcissistic( value ):
    digits = len(str(value))
    sum = 0
    backUp = value
    while value > 0:
        sum += ((value%10) ** digits)
        value = value // 10
    return sum == backUp

print(narcissistic(7))