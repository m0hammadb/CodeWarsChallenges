from itertools import permutations


def gta(limit, *args): # find the base_list first
    #your code here    # I can't get out of my mind these words "Round Robin"
    lst = []
    finished = False
    i = 0
    while not finished:
        for item in args:
            strNum = str(item)
            if(i < len(strNum)):
                cc = int(strNum[i])
                if(cc not in lst):
                    lst.append(cc)
                    if(len(lst) == limit):
                        finished = True
                        break
        i += 1
    s = 0
    for i in range(1,limit+1): 
        for item in permutations(lst,i):
            s += sum(item)

    return s




#print(allCombs([1,2,3,4]))
gta(8,12348,47,3639)