def alphabet_position(text):
    alphaDict = {}
    text = text.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alpha)):
        alphaDict[alpha[i]] = str(i + 1)
    
    final = ""
    for char in text:
        if(char in alphaDict):
            final += alphaDict[char] + " "
    
    return final[:-1]