def triangle(row):
    row = row.upper()
    myDict = {("B","G"):"R",
              ("G","B"):"R",
              ("R","G"):"B",
              ("G","R"):"B",
              ("B","R"):"G",
              ("R","B"):"G"
    }
    numDict = {"B":1,"R":2,"G":3}
    x = 0
    y = 0
    z = 0
    while True:
        print(row)
        #print(row.count("R"),row.count("G"),row.count("B"))
        nBreak = True
        newRow = ""
        sum = 0
        for i in range(len(row)-1):
            sum += numDict[row[i]]
            nBreak = False
            if(row[i] == row[i+1]):
                newRow += row[i]
            else:
                newRow += myDict[(row[i],row[i+1])]
        #print(sum)
        if(nBreak):
            break
        row = newRow

    return row

triangle("RGRRGBRGB")