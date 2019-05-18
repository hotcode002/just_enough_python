##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# Check if two words are anagrams or not
# In this program you will you understand
# 1. How sorting of a list works

first_word = input ( "First word - ")
second_word = input ( "Second word - ")

if sorted(first_word) == sorted(second_word) :
    print ( first_word, " and ", second_word, " are anagrams")
else :
    print ( first_word, " and ", second_word, " are not anagrams")

# convert the word to a list ( break it down into it's individual letters )
# and sort to compare

# if list(first_word).sort() == list(second_word).sort() :
#     print ( first_word, " and ", second_word, " are anagrams")
# else :
#     print ( first_word, " and ", second_word, " are not anagrams")    
