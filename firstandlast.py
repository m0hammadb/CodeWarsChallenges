def firstandlast1(inp):
    return inp[1:-1]

def firstandlast2(inp):
    result = ""
    for i in range(1,len(inp)-1):
        result += inp[i]
    return result

def firstandlast3(inp):
    lst = list(inp)
    lst.pop(len(inp)-1)
    lst.pop(0)
    result = ""
    for item in lst:
        result += item
    return result

print(firstandlast1("MohammadB"))
print(firstandlast2("MohammadB"))
print(firstandlast3("MohammadB"))