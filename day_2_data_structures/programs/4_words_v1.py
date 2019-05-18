##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# In this program, we will identify the common words in a list of sentences
# In this program, we will learn about
# 1. set intersection

s1 = input("First Sentence - ")
s2 = input("Second Sentence - ")

l1 = s1.split(" ")
l2 = s2.split(" ")

common_words = set(l1) & set(l2)

print ( "First sentence is ",s1)
print ( "Second sentence is ",s2)

print ( "Common words are - ", common_words)
