def count(string):
    dic = {}
    for c in string:
        if(c in dic):
            dic[c] += 1
        else:
            dic[c] = 1
    return dic