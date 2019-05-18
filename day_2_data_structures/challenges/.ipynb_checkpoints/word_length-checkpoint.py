# Count the length of each of the unique words in a sentence
# and list them in decreasing order

input_string = input ( "Enter your string - ")

# Split the string into words
words = input_string.split(" ")

# Get only the unique words
words = set(words)

# Initialize a word length ( as a dictionary)
word_count = {  }


# # Iterate through the words and start updating the word length counter
for word in words :

    # If a word is not already counted, add it to the counter
    if word_count.get(word) == None :
        word_count[word] = len(word)

# Dictionaries cannot be sorted. So, create a list of tuples or lists
t_word_count = []
for word in word_count.keys() :
    t_word_count.append( [ word, word_count.get(word) ] )

# The sort criteria is the word count
def sort_criteria(ls) :
    return ls[1]

# Now sort the list based on the inner list's word length
t_word_count.sort(key = sort_criteria)

# Default sorting order is Ascending. If you want descending, set reverse flag to True
# t_word_count.sort(key = sort_criteria, reverse = True)


# Print them out
for i in t_word_count :
    print (i[0],"----",i[1])
