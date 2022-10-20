lowerRange=int(input("Enter lower range: "))
higherRange = int(input("Enter higher range: "))

guessCount = 0

while True:
    midPoint=int((lowerRange + higherRange) / 2)
    if(higherRange - lowerRange == 0):
        probability = 100
    else:
        probability = (1/(higherRange-lowerRange)) * 100
    guessCount += 1
    
    answer = input(str(midPoint) + " ? (h/l/c) Probability: '" + str(int(probability)) + "%' : ")
    if(answer=="h"):
        lowerRange = midPoint + 1
    elif(answer== "l"):
        higherRange = midPoint - 1
    elif(answer == "c"):
        print("Hooraaaaaaaaaaaaaaaaaaaaa!!!! Guess Count: " + str(guessCount))
        break
#675123