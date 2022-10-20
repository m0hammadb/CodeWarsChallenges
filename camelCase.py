def to_camel_case(text):
    final = ""
    newWord = True
    for i in range(len(text)):
        if(i == 0):
            final += text[i]
            newWord = False
        else:
            if(text[i] != "-" and text[i] != "_"):
                if(newWord):
                    final += text[i].upper()
                    newWord = False
                else:
                    final += text[i]
            else:
                newWord = True

    return final
print(to_camel_case("The-Stealth-Warrior"))