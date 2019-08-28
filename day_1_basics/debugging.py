first_num = int (input ("first num >"))
second_num = int (input ("second num >"))
for number in range(first_num,second_num + 1):
    
    found_prime = True
    for i in range(2, number-1):
        if number % i == 0 :
            print ( number , "is not a prime number")
            found_prime = False
            break
            
    if found_prime == True :
        print ( number , "is a prime number")