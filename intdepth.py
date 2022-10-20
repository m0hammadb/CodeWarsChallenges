def compute_depth(n):
    nums = list("0123456789")
    counter = 0
    i = 1
    while len(nums) != 0:
        strNum = str(i * n)
        for c in strNum[:]:
            if(c in nums):
                nums.remove(c)

        counter += 1
        i += 1
    return counter

print(compute_depth(42))