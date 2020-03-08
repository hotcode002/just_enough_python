# Play the game continously until the user enters Ctrl + C

import sys
from random_word import RandomWords

rw = RandomWords()

print("Hangman game :")
print("Type 'exit' to quit the game")


def get_indices(list_word, letter):

    indices = []
    # iterate over the list
    for index, l in enumerate(list_word):
        if letter == l:
            indices.append(index)

    print(indices)
    return indices


try:
    # Play the game continously until the user enters Ctrl + C
    while True:
        word = rw.get_random_word(hasDictionaryDef=True, maxLength=10)
        word = list(word.upper())

        guessed_word = [" "] * len(word)

        # print (word)

        # maximum of 20 tries
        for tries in range(20):

            if guessed_word == word:
                print("Good job !! Lets move on to the next word")
                break
            # display the word with all blanks
            for index, val in enumerate(guessed_word):
                if index == len(guessed_word) - 1:
                    if val == " ":
                        print("_")
                    else:
                        print(val)
                else:
                    if val == " ":
                        print("_", end=" ")
                    else:
                        print(val, end=" ")

            # ask the user to take a guess
            letter = input("\nTake a guess--> ").upper()
            if letter.upper() == "EXIT":
                sys.exit(0)

            # if the letter the user entered is in the random word, remake the display_word to show it.
            if letter in word:
                indices = get_indices(word, letter)
                for index in indices:
                    guessed_word[index] = letter

        else:
            print("You have exceeded 20 tries. Try another word")
            print("The word is ", word)

# exit the game when the user presses Ctrl + c
except KeyboardInterrupt:
    sys.exit(0)
