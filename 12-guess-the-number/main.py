# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

go_agane = 'y'

while go_agane == 'y':
    print(art.logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100...")
    number = random.randint(0, 100)
    has_number_been_guessed = False
    DIFFICULTY_LEVELS_GUESSES = {
        "easy": 10,
        "hard": 5,
    }

    difficulty = input("Difficulty choice ('easy' or 'hard'): ")
    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input("'easy' or 'hard': ")

    lives = DIFFICULTY_LEVELS_GUESSES[difficulty]

    while not has_number_been_guessed and lives > 0:
        if lives != 1:
            print(f"you have {lives} guesses remaining")
        else:
            print("this is your last guess")

        guess = int(input("make a guess: "))

        if guess == number:
            print(f"nice, you guessed it, the number was {number}")
            has_number_been_guessed = True
        elif guess > number:
            print("too high.")
        else:
            print("too low.")

        lives -= 1

    if lives == 0 and not has_number_been_guessed:
        print(f"you ran out of lives. the number was {number}")

    go_agane = input("go again - 'y' or 'n': ")
    while go_agane != 'y' and go_agane != 'n':
        go_agane = input("go again - 'y' or 'n': ")
