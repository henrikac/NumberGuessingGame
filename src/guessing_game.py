"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


MIN_GUESS = 1
MAX_GUESS = 10
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

