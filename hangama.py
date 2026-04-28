# Hangman Game - Simple Text Based
import random

# Predefined word list
words = ["apple", "tiger", "house", "plant", "bread"]

# Randomly choose a word
word = random.choice(words)

# Create hidden word display
guessed_word = ["_"] * len(word)

# Variables
incorrect_guesses = 0
max_guesses = 6
guessed_letters = []

print("Welcome to Hangman Game!")

# Game loop
while incorrect_guesses < max_guesses and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)
    
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check correct guess
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong!")

# Final result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
