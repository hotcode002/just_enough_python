##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# This is an extension of the previous program - except
# we will rank each school by their average grade and 
# list it in that order, along with the respective grades
# for example, 
# "Sherwood Elementery school", 3.5, [3.5, 4.0, 2.9 ...]
# "Redmond Elementery school" , 3.4, [3.2, 4.1 ,3.5 ...]
# .. so on

# We could do this using 2 lists more easily, but let's work everything
# into a single list and see if we do this.

# In this program, we will learn about 
# 1. merge lists using the + operator

import math

grades_each_schools = []

# say there are 5 schools and we are calculating
# the average grade for just one class

for i in range(1,6) :
    school_name = input (" Enter the school name - ") 
    school_grades = []
    school_grades.append(school_name)
    print ( "Enter the grades for this school (e to exit ) -")
    grades = []
    while True :
        grade = input ( " - ")
        if grade == "e" :
            break
        else :
            grades.append(float(grade))
    school_grades.append(grades)
    grades_each_schools.append(school_grades)

print ( grades_each_schools)

for school in grades_each_schools :
    average = math.fsum(school[1]) / len(school[1])
    school.insert(0,average)

print ( grades_each_schools)

# sort the school by average grade in reverse order
grades_each_schools.sort( reverse = True)

# pretty up the printing
# for school in grades_each_schools :
#     print (school[0],"\t\t",school[1],"\t\t\t\t",school[2])

# or better
print ('{:<10} {:<50} {:<30} '.format("Avg. Grade","School Name","Grades") )
for school in grades_each_schools :
    print ('{:<10} {:<50} {:<30} '.format(school[0],school[1],str(school[2])) )