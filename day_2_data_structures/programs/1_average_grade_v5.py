##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# Say you are calculating the average grade across the entire district
# Each school has a separate list of grades, we just have to calculate 
# the average across all the lists( school ). Just for simplicity, let's 
# assume we are calculating grades for just Class 1 across all the schools

# In this program, we will learn about 
# 1. merge lists using the + operator

import math

grades_each_schools = []

# say there are 5 schools
for i in range(1,6) : 
    print ( "Enter grades of each student for school ",i," - 'e' to exit")
    grades = []
    while True :
        grade = input ( " - ")
        if grade == "e" :
            break
        else :
            grades.append(float(grade))
    
    grades_each_schools.append(grades)

grades_all_schools = []
for grades in grades_each_schools :
    grades_all_schools += grades

average = math.fsum(grades_all_schools) / len(grades_all_schools)
print ( "Average grade of all 5 schools is - ", average)


