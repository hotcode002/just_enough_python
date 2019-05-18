##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# In this program, we will find out the following in sentence.
# 1. List all the words that contain a particular vowel
# 2. List the same against each of the vowel
# 
# Learning - 
#   In this program, we will be learning about compound data structures
#       1. That a dictionary value can be another data structure ( like a list )

sentence = input ( "Enter a sentence -")
words    = sentence.split(" ")

vowels = ['a','e','i','o','u']
vowel_words = {}

for word in words :
    for letter in list(word) :
        if letter in vowels :
                if vowel_words.get(letter) == None :
                        vowel_words[letter] = [word]
                else :
                        vowel_words.get(letter).append(word)

print ( vowel_words )
