##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# This is a rewrite of the average grade program we have done previously. 
# In this program, we will learn about 
# 1. modify lists
# 2. delete elements in list
# 3. clear lists
# 4. remove specific elements in list

import math

# create an empty grades list
grades = []

# initialize sum of grades to 0. 
sum    = 0

print ( " enter your choices - ")
while ( True ) :
    print ( "Enter your choice - ")
    print ( "- 'enter' grades")
    print ( "- 'delete' grades")
    print ( "- 'update' grades")
    print ( "- 'clear' grades")
    print ( "- calculate 'average'")
    print ("- 'exit'")
    
    choice = input("- ")
    if choice == "exit" :
        break
    
    if choice == "enter" :
        print ( "Enter grades. type e to exit")
        while True :
            grade = input ( " --> ")
            if grade == "e" :
                break
            else :
                grade   = float(grade)
                grades.append(grade)
        print ( "You have entered - ")
        print ( grades )

    if choice == "delete" :
        if len(grades) == 0 : 
            # there are no grades yet. 
            print ( " No grades input yet. Please try to input grades")
        else :
            print ( "Enter index to delete. type e to exit")
            while True or len(grades) != 0 :
                index = 0
                print ( "index - grade")
                for grade in grades :
                    print ( index,"\t",grade)
                    index = index + 1
                
                grade = input ( "-->")
                if grade == "e" :
                    break
                else :
                    if int(grade) < len(grades) :
                        grades.pop(int(grade))
    
    if choice == "update":
        if len(grades) == 0 : 
            # there are no grades yet. 
            print ( " No grades input yet. Please try to input grades")
        else :
            print ( "Enter index to update. type e to exit")   
            while True or len(grades) != 0 :
                index = 0
                print ( "index - grade")
                for grade in grades :
                    print ( index,"\t",grade)
                    index = index + 1             

                grade = input ( "-->")
                if grade == "e" :
                    break
                else :
                    if int(grade) < len(grades) :
                        print ( "Changing grade")
                        print ( "--------------")
                        print ( "index - grade")
                        print ( int(grade), "\t",grades[int(grade)])
                        print ( "enter new grade")
                        new_grade = input( "-->")
                        grades[int(grade)] = float(new_grade)          

    if choice == "clear" :
        if len(grades) == 0 : 
            # there are no grades yet. 
            print ( " No grades input yet. Please try to input grades")   
        else :
            grades.clear()
            print ( "cleared all grades") 
            print ( "=================")        

    if choice == "average" :
        average = math.fsum(grades) / len(grades)
        print ("Average --> ",average)    
        print ("=================")           


                