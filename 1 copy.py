#whether it is a perfect number or not.

number = int(input("Please enter a natural number: "))

divisors = []
sum = 0
i = 1 
while i < number:
    if number % i == 0:
        divisors.append(i)
        sum += i
        i += 1
    elif number != 0:
        i +=1
    
print("Divisors = ",divisors)
print("The summation of less than or equal divisors of number = ",sum)

    
if sum == number:
    print("Woww, {} is a perfect number.".format(number)) 
else:
    print("No perfect number.")


    


