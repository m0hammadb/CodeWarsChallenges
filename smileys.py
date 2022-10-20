def count_smileys(arr):
    starters = [":",";"]
    midds = ["-","~"]
    finishers = ["D",")"]

    allgoods = [":",";","-","~","D",")"]
    counter = 0
    for item in arr:
        good = True
        for c in item:
            if(c not in allgoods):
                good = False
        if(good):
            if(item[0] in starters and item[-1] in finishers):
                counter += 1
    return counter

print(count_smileys([';]', ':[', ';*', ':$', ';-D']))