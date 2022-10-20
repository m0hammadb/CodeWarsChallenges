def decimalToHex(decimal):
    hexDict = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    hexR = ""
    while decimal > 0:
        rm = decimal % 16
        decimal = decimal // 16
        if(rm > 9):
            hexR = hexDict[rm] + hexR
        else:
            hexR = str(rm) + hexR
    ln = len(hexR)
    for i in range(2-ln):
        hexR = "0" + hexR
    return hexR
def validation(inp):
    if(0 <= inp <= 255):
        return inp
    else:
        if(abs(inp - 255) > abs(inp - 0)):
            return 0
        else:
            return 255
def rgb(r, g, b):
    return decimalToHex(validation(r)) + decimalToHex(validation(g)) + decimalToHex(validation(b))

print(rgb(-20, 275, 125))