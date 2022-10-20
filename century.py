def century(year):
    rem = 0
    if(year % 100 > 0):
        rem = 1
    return (year // 100) + rem

print(century(50321))