"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import os
import random
import sys


MIN_GUESS = 1
MAX_GUESS = 10

# checks if the player specifiy a new MAX_GUESS in command line
# i.e.:     python guessing_game.py 100
# sets MAX:GUESS to specified value if valid
if len(sys.argv) == 2:
    try:
        new_max = int(sys.argv[1])

        if new_max > 10:
            MAX_GUESS = new_max
        else:
            raise ValueError('The new MAX_GUESS has to be greater than 10')
    except ValueError as err:
        print(f'Invalid argument: {err}\n')
        exit(1)

def clear_console():
    os.system('cls') if os.name == 'nt' else os.system('clear')


def welcome():
    print('Welcome to the Number Guessing Game!')
    print('------------------------------------')
    print(f'Guess a number between {MIN_GUESS} and {MAX_GUESS}\n')


def display_highscore(highscore):
    if highscore == 0:
        highscore = '---'
    print(f'Current highscore: {highscore}\n')


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


def play():
    CORRECT_NUM = random.randint(MIN_GUESS, MAX_GUESS)
    num_guesses = 0
    still_guessing = True

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
    return num_guesses


def play_again():
    play_again = input('\nDo you want to play again ([y]es / [n]o)? ')
    if play_again.lower() == 'y':
        return True
    return False


def update_highscore(highscore, num_guesses):
    if highscore == 0 or num_guesses < highscore:
        return num_guesses
    return highscore


def start_game():
    still_playing = True
    highscore = 0

    while still_playing:
        clear_console()
        welcome()
        display_highscore(highscore)
        num_guesses = play()

        if not play_again():
            still_playing = False
        highscore = update_highscore(highscore, num_guesses)
    print('Goodbye\n')
    

if __name__ == '__main__':
    start_game()

