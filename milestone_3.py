import random

# List of words
word_list = ["Apple", "Orange", "Strawberry", "Blueberry", "Blackberry"]

# Select a random word
word = random.choice(word_list)

# Ask the user to guess a letter and validate it
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
                print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess) # Calls check_guess function

# Function to check if the letter is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry. {guess} is not in the word. Try again.")   

ask_for_input()   