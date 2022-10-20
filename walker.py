def is_valid_walk(walk):
    x = 0
    y = 0
    counter = 0
    for step in walk:
        if(step == 'n'):
            y += 1
        elif(step == 's'):
            y -= 1
        elif(step == 'e'):
            x += 1
        else:
            x -= 1
        counter += 1
    
    if(counter == 10 and x == 0 and y == 0):
        return True
    else:
        return False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n']))