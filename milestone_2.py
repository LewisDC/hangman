import random

# List of words
word_list = ["Apple", "Orange", "Strawberry", "Blueberry", "Blackberry"]

# Select a random word
word = random.choice(word_list)
print(word)
# Ask the user to guess a letter

guess = input("Enter a letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops, That is not a valid input")

