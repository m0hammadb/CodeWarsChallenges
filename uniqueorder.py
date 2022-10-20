def unique_in_order(iterable):
    lastChar = ""
    rValue = []
    for char in iterable:
        if(char != lastChar):
            lastChar = char
            rValue.append(char)
    return rValue