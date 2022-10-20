def count_bits(n):
    count = 0
    while n > 0:
        if(n % 2 == 1):
            count += 1
        n = n // 2
    return count

print(count_bits(1234))