"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import sys


MIN_GUESS = 1
MAX_GUESS = 10

# checks if the player specifiy a new MAX_GUESS in command line
# i.e.:     python guessing_game.py 100
# sets MAX:GUESS to specified value if valid
if len(sys.argv) > 1:
    try:
        new_max = int(sys.argv[1])

        if new_max > 1:
            MAX_GUESS = new_max
    except ValueError:
        pass

CORRECT_NUM = random.randint(MIN_GUESS, MAX_GUESS)

def welcome():
    print('Welcome to the Number Guessing Game!')
    print('------------------------------------')
    print(f'Guess a number between {MIN_GUESS} and {MAX_GUESS}\n')


def prompt_for_guess():
    while True:
        guess = input('Enter a number: ')
        try:
            guess = int(guess)

            if guess < MIN_GUESS or guess > MAX_GUESS:
                raise ValueError(f'Please only enter a number between {MIN_GUESS} and {MAX_GUESS}')
        except ValueError as err:
            print(f'Invalid input: {err}')
        else:
            return guess


def start_game():
    num_guesses = 0
    still_guessing = True

    welcome()

    while still_guessing:
        num_guesses += 1
        guess = prompt_for_guess()

        if guess == CORRECT_NUM:
            print(f'\nCongratulations! You guesses the number in {num_guesses} tries!')
            still_guessing = False
        elif guess < CORRECT_NUM:
            print('The number is higher')
        else:
            print('The number is lower')
    print('Goodbye\n')
    

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

