import random

# List of words
word_list = ["Apple", "Orange", "Strawberry", "Blueberry", "Blackberry"]

# Select a random word
def choice():
    word = random.choice(word_list)
    return word

# Ask the user to guess a letter
def user_guess():
    guess = input("Enter a letter")
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        return guess
    else:
        print("Oops, That is not a valid input")

