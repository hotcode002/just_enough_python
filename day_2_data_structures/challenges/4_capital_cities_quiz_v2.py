##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# This is an enhanced version of version 1

import csv
import random

file = open( "./data/capital_cities.csv" )
capital_cities = csv.reader ( file )

# Put the entries into a dictionary ( Country : Capital City) format
capital_cities_d = {}
for row in capital_cities : 
    capital_cities_d[row[0]] = row[1]

# Delete the first row
del capital_cities_d['Country']

# capitalize to ensure user errors are accomodated for
def str_comparision (user_answer, correct_answer) :
    if user_answer.upper() == correct_answer.upper() : 
        return True
    else :
        return False

# stay in this loop for ever until the user enters "exit"
while ( True ) : 
    country = random.choice( list(capital_cities_d.keys()))
    answer = input ( 'what is the capital of '+ country + " - ")
    if answer.upper() == "EXIT" :
        break
    answer = str_comparision ( answer , capital_cities_d.get(country))
    if answer == True :
        print ( " correct ")
    else : 
        print ( " incorrect ")

