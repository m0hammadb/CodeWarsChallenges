def init_dict():
    leftChars = "sbpw"
    rightChars = "zdqm"
    myDict = {}
    for i in range(len(leftChars)):
        myDict[leftChars[i]] = i + 1
    for i in range(len(rightChars)):
        myDict[rightChars[i]] = -(i + 1)
    return myDict

def init_wololo():
    leftChars = "sbpw"
    rightChars = "zdqm"
    myDict = {}
    for i in range(len(leftChars)):
        myDict[leftChars[i]] = rightChars[i]
        myDict[rightChars[i]] =leftChars[i]
    return myDict

    
gDictionary = init_dict()
wololoDict = init_wololo()
def get_nobomb_string(inp):
    leftChars = "sbpw"
    rightChars = "zdqm"
    rValue = ""
    for i in range(len(inp)):
        leftbomb = False
        rightbomb = False
        if(i>0):
            if(inp[i-1] == "t" and inp[i] in rightChars):
                leftbomb = True
                if(i + 1 < len(inp)):
                    if(inp[i+1] == "j"):
                        leftbomb = False
            
            if(inp[i-1] == "j"  and inp[i] in leftChars):
                leftbomb = True
                if(i + 1 < len(inp)):
                    if(inp[i+1] == "t"):
                        leftbomb = False
        
        if(i < len(inp) - 1):
            if(inp[i + 1] == "t" and inp[i] in rightChars):
                rightbomb = True
                if(i - 1 >= 0):
                    if(inp[i-1] == "j"):
                        rightbomb = False
            if(inp[i + 1] == "j" and inp[i] in leftChars):
                rightbomb = True
                if(i - 1 >= 0):
                    if(inp[i-1] == "t"):
                        rightbomb = False

        
        if(leftbomb or rightbomb):
            if(inp[i] in wololoDict):
                rValue += wololoDict[inp[i]]
            else:
                rValue += "_"
        elif(inp[i] == "t" or inp[i] == "j"):
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

#main()
print(calculate_war_score("jz"))
