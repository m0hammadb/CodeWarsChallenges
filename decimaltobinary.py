def decimalToBinary(dNumber):
    if(dNumber == 0):
        return "0"
    
    return   decimalToBinary(dNumber // 2) + str(dNumber % 2)


print(decimalToBinary(134))