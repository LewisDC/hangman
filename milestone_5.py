import random

class Hangman:

    '''
    Hangman Game Class

    This class represents a simple Hangman game. The game randomly selects a word from a given list of words,
    and the player has to guess the letters in the word within a limited number of attempts (lives). The game
    ends when the player either guesses all the letters correctly or runs out of lives.

    Attributes:
        word_list (list): A list of words from which the game randomly selects the secret word.
        num_lives (int): The number of lives the player starts with (default is 5).
        list_of_guesses (list): A list of letters guessed by the player.
        word (str): The randomly selected word to be guessed.
        word_guessed (list): A list representing the current status of the word being guessed, with underscores
                            for unguessed letters and correct letters revealed.
        num_letters (int): The number of unique letters in the word that have not been guessed yet.

    Methods:
        pick_random_word(): Selects a random word from the word_list attribute.
        check_guess(guess): Checks if the guessed letter is in the secret word and updates the game status.
        ask_for_input(): Prompts the player to guess a letter and manages player input and game outcomes.
    '''


    def __init__(self, word_list, num_lives = 5):
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = self.pick_random_word()
        self.word_guessed = ["_"] * len(self.word)
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
                if letter == guess:
                    # set the underscore at that position to the correct letter
                    self.word_guessed[i] = letter
            # print current status of the secret word
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
            # check if the guess is a single letter         
            if len(guess) != 1 or not(guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            # check if letter has already been guessed
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                # add the guessed letter to the list of guesses
                self.list_of_guesses.append(guess)

                # when number of lives reach zero, the player loses
                if self.num_lives == 0:
                    print("You lost!")
                    return False
                
                # when the player has guessed all the letters, the player wins
                elif self.num_letters == 0:
                    print(f"{''.join(self.word_guessed)} is correct!")
                    print("Congradulations. You won the game!")
                    return True

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        # Check if the player loses and break the loop
        if game.num_lives == 0:
            break
        # Call ask_for_input and break if it returns True (game won)
        elif game.ask_for_input():
            break

word_list = ["apple", "orange", "strawberry", "blueberry", "blackberry", "banana", "grape", "grapefruit", "mango", "pear", "raisin", "current", "peach", "kiwi"]
play_game(word_list)