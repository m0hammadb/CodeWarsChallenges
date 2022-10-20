
def lcs(str1,str2):
    matches = []
    startIndex = 0
    lastPoint = -1
    currentSub = ""
    while True:
        for i in range(startIndex,len(str2)):
            letterPoint = str1.find(str2[i],lastPoint+1)
            
            if(letterPoint != -1):
                currentSub += str2[i]
        
        currentSub = ""
        lastPoint = -1


a = "abcefgidx"
b = "bdfx"