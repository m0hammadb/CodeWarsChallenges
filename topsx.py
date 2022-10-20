def tops(msg):
    stepper = 5
    nextCharPosition = 1
    final = ""
    for i in range(len(msg)):
        if i == nextCharPosition:
            final += msg[i]
            nextCharPosition += stepper 
            stepper += 4
    
    return final[::-1]