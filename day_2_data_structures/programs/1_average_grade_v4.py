##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# Instead of calculating grades for just one class, let's calculate
# the average of grades across classes 1 to 

# In this program, we will learn about 
# 1. compound lists ( list of lists )
# 2. enumerator

import math

grades_all = []

for i in range(1,6) : 
    print ( "Enter grades of each student for grade ",i," - 'e' to exit")
    grades = []
    while True :
        grade = input ( " - ")
        if grade == "e" :
            break
        else :
            grades.append(float(grade))
    
    grades_all.append(grades)

for index, grades in enumerate(grades_all) :
    average = math.fsum(grades) / len(grades)
    print ( "Average grade of class ", index, " is - ", average)


