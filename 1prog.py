# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random
import sys

num_picks = 3
min_picks = 0
max_picks = 100
Price = 5,000,000

def note():
    from time import sleep
    string=("      Welcome to Aleja's Lottery 🎊      ")
    for letter in string:
        sleep (0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()
        separator()

        _name = input("   Kindly enter you name>> ")
        print(f" Hello {_name} !")
        print("Are you ready to play and win?")

def attempt():
    resp_= input("/n Please enter Yes or No >>")
    print("/n")
    if resp_.lower() == "Yes":
        quote()
        return attempt
    elif attempt.lower() == "No":
        separator()
        print("Okay, take your time ! You can come back when you are ready")
        print("You can exit the game now")
        separator()
        sys.exit("/n")
    else: 
        print("Sorry ! You must enter Yes/No")
        return attempt()

def separator():
    print("-----------------------------------------------")

def quote():
    from time import sleep
    string = ("/n/t “Life is a lottery that we've already won. /n/t But most people have not cashed in their tickets. /n/t")
    for letter in string:
        sleep (0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()



def main():
    note()
    separator()
    attempt()


main()