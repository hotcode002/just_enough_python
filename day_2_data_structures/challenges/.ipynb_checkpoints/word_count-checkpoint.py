# Count the number of occurrences of each of the words in a sentence

input_string = input ( "Enter your string - ")

# Split the string into words
words = input_string.split(" ")

# Initialize a word counter ( as a dictionary)
word_count = {  }


# # Iterate through the words and start updating counts
for word in words :

    # If a word is not already counted, add it to the counter
    if word_count.get(word) == None :
        word_count[word] = 1
    # If already present, increment the word count
    else :
        word_count[word] = word_count[word] + 1

# Finally, print the counter
print ( word_count)
