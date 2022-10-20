def init_dict():
    leftChars = "sbpw"
    rightChars = "zdqm"
    myDict = {}
    for i in range(len(leftChars)):
        myDict[leftChars[i]] = i + 1
    for i in range(len(rightChars)):
        myDict[rightChars[i]] = -(i + 1)
    return myDict


gDictionary = init_dict()

def get_nobomb_string(inp):
    rValue = ""
    for i in range(len(inp)):
        leftbomb = False
        rightbomb = False
        if(i>0):
            if(inp[i-1] == "*"):
                leftbomb = True
        
        if(i < len(inp) - 1):
            if(inp[i + 1] == "*"):
                rightbomb = True
        
        if(leftbomb or rightbomb or inp[i] == "*"):
            rValue += "_"
        else:
            rValue += inp[i]
    
    return rValue

def calculate_war_score(inp):
    inp = get_nobomb_string(inp)
    score = 0
    for char in inp:
        if(char in gDictionary):
            score += gDictionary[char]
    return score

def main():
    warCode = "z**z" #change this for different results
    warScore = calculate_war_score(warCode)

    if(warScore == 0):
        print("Damn! We will have to fight again!")
    elif(warScore > 0 ):
        print("Yay! Left Side Won!")
    else:
        print("Wow! Right Side Won")

main()

