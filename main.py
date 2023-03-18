import random

# Define a list of words for the game
words = ['python', 'code', 'programming', 'computer', 'algorithm', 'variable', 'function']

# Choose a random word from the list
word = random.choice(words)

# Define a function to display the current state of the game
def display_game_state(letters):
    for letter in word:
        if letter in letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

# Define the game loop
letters_guessed = []
while True:
    # Display the current state of the game
    display_game_state(letters_guessed)
    
    # Check if the player has guessed all the letters
    if set(word) <= set(letters_guessed):
        print("Congratulations, you guessed the word!")
        break
    
    # Prompt the player to guess a letter
    guess = input("Guess a letter: ").lower()
    
    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess, please enter a single letter.")
        continue
    
    # Check if the letter has already been guessed
    if guess in letters_guessed:
        print("You already guessed that letter, try again.")
        continue
    
    # Add the letter to the list of guessed letters
    letters_guessed.append(guess)
    
    # Check if the letter is in the word
    if guess in word:
        print("Good guess!")
    else:
        print("Sorry, that letter is not in the word.")