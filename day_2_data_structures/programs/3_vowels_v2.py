##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# In this program, we will find out the count of the each of the vowels
# in a sentence.
# Learning - 
#   In this program, we will be learning
#       1. How to get initialize a dictionary
#       2. How to insert a key,value pair
#       3. How to check if a key exists

sentence = input ( "Enter a sentence -")

vowels = ['a','e','i','o','u']
vowel_count = {}

for i in list(sentence) :
    if i in vowels :
        if vowel_count.get(i) == None :
                vowel_count[i] = 1
        else :
                vowel_count[i] = vowel_count[i] + 1

print ( vowel_count )