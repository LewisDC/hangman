import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        # List of words
        self.word_list = word_list
        # Number of lives the player has at the start of the game
        self.num_lives = num_lives
        # A list of the guesses that have already been tried
        self.list_of_guesses = []
        # Select a random word
        self.word = self.pick_random_word()
        # Blank list of underscores to store and display the guessed letters
        self.word_guessed = ["_"] * len(self.word)
        # Number of unique letters that have not been guessed yet
        self.num_letters = len(set(self.word))

    def pick_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # loop through the letters in self.word
            for i, letter in enumerate(self.word):
                # check if the current looped letter is equal to the guess
                if letter != "_" and guess == letter:
                    # set the underscore at that position to the correct letter
                    self.word_guessed[i] = letter
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry. {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        print(self.word_guessed)
        while True:
            guess = input("Guess a letter: ")            
            if len(guess) != 1 or not(guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess) # Calls check_guess function
                self.list_of_guesses.append(guess)


word_list = ["apple", "orange", "strawberry", "blueberry", "blackberry", "banana", "grape", "grapefruit", "mango"]
hangman = Hangman(word_list)

hangman.ask_for_input()