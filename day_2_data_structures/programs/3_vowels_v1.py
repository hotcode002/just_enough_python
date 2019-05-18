##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# In this program, we will find out how many vowels are there in a sentence.
# Learning - 
#   In this program, we will be learning
#       1. How to search for values in a list

sentence = input ( "Enter a sentence -")

vowels = ['a','e','i','o','u']
vowel_count = 0

for i in list(sentence) :
    if i in vowels :
        vowel_count += 1

print (" The number of vowels in the sentence is - ", vowel_count)