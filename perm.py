def perm(inp,caller,lst):
    
    if(inp == ""):
        lst.append(caller)
        return lst

    for i in range(len(inp)):
        c = inp[i]
        remain = inp[:i] + inp[i+1:]
        perm(remain,caller + c,lst)
        

    return lst

def permutations(inp):
    lst = []
    return list(set(perm(inp,"",lst)))

print(permutations("abba"))