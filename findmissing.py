def find_missing_letter(chars):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if(chars[0].upper() == chars[0]):
        alpha = alpha.upper()
    
    nextLetter = alpha.find(chars[0]) + 1
    for i in range(1,len(chars)):
        if(chars[i] != alpha[nextLetter]):
            return alpha[nextLetter]
        else:
            nextLetter += 1

print(find_missing_letter(['O','Q','R','S']))

