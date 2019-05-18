##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# In this program we will learn
# 1 - Dictionary Data Structure
# 2 - Functions

import random

q = {"The capital of India is New Delhi": True,
     "The capital of China is Shanghai" : False,
     "The capital of Australia is Canberra" : True,
     "The capital of Brazil is Rio de Janiera": False,
     "The capital of United States is New York" : False,
     "The capital of Russia is St. Petersburg" : False,
     "The capital of Singapore is Singapore" : True
    }

def str_to_bool (s ) :
    if s == "true" or s == "True" :
        return True
    elif s == "false" or s == "False" :
        return False


while ( True ) : 
    question = random.choice( list(q.keys()))
    answer = input ( question + " - ")
    answer = str_to_bool ( answer)
    if answer == q.get(question) :
        print ( " correct ")
    else : 
        print ( " incorrect ")