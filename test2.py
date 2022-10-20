def hex_to_dec(s):
    chars = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    s = s[::-1].upper()
    final = 0
    for i in range(len(s)):
        c = 0
        if(s[i] in chars):
            c = chars[s[i]]
        else:
            c = int(s[i])
        final +=  c * (16 ** i)
    
    return final

lst = [1,2,3]

def myLen(myData):
    return myData.__len__()

print(myLen(lst))
print(myLen("abc"))
print(myLen(12))
