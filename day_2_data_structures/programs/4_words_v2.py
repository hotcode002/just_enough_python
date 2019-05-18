##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# Give 2 sentences, identify
# 1. common words between the sentences
# 2. unique words across the sentences
# 3. words in first sentence that are not present in the second.
# 4. unique words across the sentences excluding the common words.

# In this program, we will learn about
# 1. set intersection
# 2. set union
# 3. set difference
# 4. multiple operations on sets

s1 = input("First Sentence - ")
s2 = input("Second Sentence - ")

# split and store in lists
l1 = s1.split(" ")
l2 = s2.split(" ")

# set intersection
common_words = set(l1) & set(l2)

# set union
unique_words = set(l1) | set(l2)

# set difference
first_not_second = set(l1) - set(l2)

# combine sets
unique_exclude_common = ( set(l1) | set(l2) ) - (set(l1) & set(l2) )

print ( "First sentence is ",s1)
print ( "Second sentence is ",s2)

print ( "Common words are - ", common_words)
print ( "unique words are - ", unique_words)
print ( "unique words in first that are not there in the second sentence - ", first_not_second)
print ( "unique words across sentences, excluding common words - ", unique_exclude_common)
