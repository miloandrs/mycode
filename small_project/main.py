#!/usr/bin/env python3
from dictionaries import *
from functions import *
from random import choice
"""
Camilo Castro
Project script to a vocabulary enhancement game.
"""


#Run-time code
def main():
    #iterator for the game
    while True:
        # print for the word. 
        print(choice(word_pool))
        print("")
        user_collection()
        print(f'Hello {user["name"]}.')
        



        if input == "q":
            break



#Call main function
if __name__ == "__main__":
    main()
