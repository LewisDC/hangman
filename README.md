# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 1: Set up the environment

In this project, we'll use GitHub to track changes to our code and save them online in a GitHub repo called hangman

## Milestone 2: Create the variables for the game

* Created a local version of the repo with *git clone*
* Created a file named **milestone_2.py** which will contrain the code for this milestone.
* Created a list of words, in this case 5 fruits and assigned the list to a variable called **word_list**.
* Imported the **random** module.
* Used the **random.choice** method to assign a random word from **word_list** to the variable **word**, which will serve as the secret word.
* Used the **input()** method to request a letter from the user and assign it to the variable **guess**
* Created an **if** statement that checks if the length of the input is equal to 1 and is alphabetical:

![Alt text](image-1.png)

* Created a **README.md** file and began documenting my experience
* Uploaded files to Github repo

## Milestone 3: Check if the guessed character is in the word

* Used a **while** loop to continuously ask the user for a letter and validate it, using the code from the image in milestone 2
* Check if the guess is in the secret word with **'if guess in word:'** statement which feeds back to the user accordingly
* Created the **check_guess** function which converts the users guess to lower case using the **lower()** string method, and then performs the above check.
* Created the **ask_for_input** function which asks the user for a letter, validates it, then calls **check_guess**

## Milestone 4: Create the Game class