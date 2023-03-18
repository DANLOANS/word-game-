import random

# Define a list of words for the game
words = ["python", "programming", "coding", "algorithm", "variable", "function"]

# Choose a random word from the list
word = random.choice(words)

# Create a list to store the guessed letters
guessed_letters = []

# Define the maximum number of incorrect guesses
max_incorrect_guesses = 6

# Define a function to display the current state of the game
def display_game_state():
    # Display the current word with underscores for unguessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)
    
    # Display the guessed letters
    print("Guessed letters:", " ".join(guessed_letters))
    
    # Display the remaining number of incorrect guesses
    incorrect_guesses = len([letter for letter in guessed_letters if letter not in word])
    print("Incorrect guesses:", incorrect_guesses, "/", max_incorrect_guesses)

# Define the game loop
while True:
    # Display the current state of the game
    display_game_state()
    
    # Check if the player has won
    if all(letter in guessed_letters for letter in word):
        print("Congratulations, you won!")
        break
    
    # Check if the player has lost
    incorrect_guesses = len([letter for letter in guessed_letters if letter not in word])
    if incorrect_guesses >= max_incorrect_guesses:
        print("Sorry, you lost. The word was", word)
        break
    
    # Prompt the player to guess a letter
    guess = input("Guess a letter: ")
    
    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess, please enter a single letter.")
        continue
    
    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter, please try again.")
        continue
    
    # Add the guessed letter to the list
    guessed_letters.append(guess)