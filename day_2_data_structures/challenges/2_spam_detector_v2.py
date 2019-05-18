##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# Given a sentence, and a list of spam words, find out
# 1. A spam score of the sentence.

# In this program, we will learn about
# 1. Open and close files
# 2. read files line by line
# 3. specify a range of numbers
# 4. delete elements from a list ( specific elements or the last element )

s = input("Input a sentence - ")

file = open ("./data/spam_words.txt")

# Read the spam words file
spam_words = []
try :
    line = file.readline()
    while line :
        spam_words.append(line.strip())
        line = file.readline()
finally : 
    file.close()

# Remove the credits
del spam_words[0:4]

# Remove the contact message at the bottom
spam_words.pop()

counter = 0
for word in spam_words :
    if s.upper().count(word.upper()) > 0 :
        counter += 1

if counter == 0 :
    print ("not spam")
else :
    print ( "spam")
        