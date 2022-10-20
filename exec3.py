from random import randint
import time

def countChars(inp,char):
    count = 0
    for c in inp:
        if(c == char):
            count += 1
    
    return count 

def createRandomString(length):
    alpha = "abcdefghiklmnopqrstuvwxyz"
    final = ""
    lst = []
    for i in range(length):
        final += alpha[randint(0,len(alpha)-1)]
    return final

#sent = "mohammad is comming! :D"
sent = createRandomString(10000000)

start_time = time.time()
myDict = {}
for c in sent:
    if(c in myDict):
        myDict[c] += 1
    else:
        myDict[c] = 1

msg = ""
for k in myDict:
     msg += k + " ==> " + str(myDict[k]) + " "
print(msg)


print("--- %s seconds ---" % (time.time() - start_time))