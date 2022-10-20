def two_sum(numbers, target):
    dic = {}
    i = 0
    for n in numbers:
        if(n in dic):
            return [i,dic[n]]
        dic[target - n] = i
        i += 1
    return []

print(two_sum([1234,5678,9012],14690))