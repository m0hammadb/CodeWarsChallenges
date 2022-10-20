def likes(name):
    template = "{} {} this"
    final = ""
    if(name == []):
        name = ["no one"]
    if(len(name) == 1):
        final = template.format(name[0],"likes")
    else:
        nameTemp = ""
        if(len(name) == 2):
            nameTemp = f"{name[0]} and {name[1]}"
        elif(len(name) == 3):
            nameTemp = f"{name[0]}, {name[1]} and {name[2]}"
        else:
            nameTemp = f"{name[0]}, {name[1]} and {len(name) - 2} others"
        final = template.format(nameTemp,"like")
    return final

print(likes(["a","b","c","d","e"]))