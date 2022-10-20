def valid_braces(string): # [({})](]
    currentKey = ""
    corrects = {"{":"}","[":"]","(":")"}
    queue = []
    for char in string:
        if(char in corrects):
            currentKey = char
            queue.append(char)
        else:
            if(currentKey == "" or char != corrects[currentKey]):
                return False
            else:
                if(queue):
                    queue.pop()
                else:
                    return False
                if(queue):
                    
                    currentKey = queue[-1]
    if(not queue):
        return True
    else:
        return False

print(valid_braces(")(}{]["))
