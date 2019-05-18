##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# Given a sentence, and a list of spam words, find out
# 1. A spam score of the sentence.

# In this program, we will learn about
# 1. Exceptions
# 2. continue statement in a loop

s = input("Input a sentence - ")

spam_words = {  "lottery"   : 9,
                "won"       : 8,
                "viagra"    : 10,
                "free"      : 8,
                "trial"     : 8,
                "scam"      : 10,
                "pharmacy"  : 7,
                "unlimited" : 7,
                "nigerian"  : 6}

words = s.split(" ")
spam_counter = 0

# Why does this throw an exception ?
# for word in words :
#     count = spam_words[word]
#     if count != None :
#         spam_counter += count


# How to handle exceptions
# for word in words :
#     try:
#         count = spam_words[word]
#     except KeyError:
#         continue
#     spam_counter += count


# .get() method implicitly handles the KeyError exception
for word in words :
    count = spam_words.get(word)
    if count != None :
        spam_counter += count

if spam_counter/len(words) < 1 :
    print ( "Not spam")
else :
    print ( "Spam")
