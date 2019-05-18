##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# Learning - 
#   In this program, we will be learning
#       1. How to take a list of numbers from the user
#       2. Sort them
# Questions -
#   1. what would happen if you did not type cast the user input to int 

print ( "Enter numbers to sort. type exit when done")

user_list = []
while ( True ) :
    i = input ("- ")
    if i.upper() == "EXIT" :
        break
    user_list.append(int(i))

user_list.sort()

print ( " here is your sorted list of numbers  - ")
print ( user_list)