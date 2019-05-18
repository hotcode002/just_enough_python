##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# This is a rewrite of the average grade program we have done on day 2
# In this program, we will learn about 
# 1. list data structure
# 2. Iterate over a list
# 3. Length of a list

# Needed in case you don't want to iterate over the list to calculate sum of floats
# import math

print ( "Enter grades to calculate mean/average grade. type e to exit")

# Create an empty list
grades = []
sum    = 0
while True :
    grade = input ( " - ")
    if grade == "e" :
        break
    else :
        grade   = float(grade)
        grades.append(grade)

# iterate through the list to calculate average
for grade in grades :
    sum = sum + grade

average = sum / len(grades)

# You can also use
# 1. Built in sum function ( for integers )
# 2. or math.fsum function ( since these are floats )

# average = math.fsum(grades) / len(grades)

print ( "Average class grade is ",average)

