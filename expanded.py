def expanded_form(num):
    powr = len(str(num)) - 1
    r = ""
    for c in str(num):
        nextInt = int(c) * (10 ** powr)
        if(nextInt > 0):
            r += str(nextInt)
            if(powr >= 1):
                r += " + "
        powr -= 1

    if(r.endswith(" + ")):
        r = r[:-3]    
    return r

print(expanded_form(721))
