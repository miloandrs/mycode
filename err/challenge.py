#!/usr/bin/env python3
import random
"""
Camilo Castro
"""


#Run-time code
def main():
    #random number generator
    num = random.randint(1,100)
    #user guess initializer
    guess = ''
    #rounds counter
    rounds= 0
    #loop for the game
    while rounds < 5 and guess != num:
        guess = input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess = int(guess)
        else:
            continue
        if guess > num:
            print("Too high!")
            rounds + 1
        if guess < num:
            print("Too low!")
            rounds + 1
        else:
            print("Correct!")


#Call main function
if __name__ == "__main__":
    main()
