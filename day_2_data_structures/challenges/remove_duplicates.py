# In this program, we will remove duplicate elements from a list

l = []
# Let the user enter some string
while True :
    i = input("-")
    if i == "e" or i == "exit" :
        break
    else :
        l.append(i)

# Print the user entered list of values
print (l)

# Convert the list to a set. This will eliminate all duplicates
# just due to the nature of a set
s = set(l)
print (s)


