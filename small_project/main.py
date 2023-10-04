#!/usr/bin/env python3
from dictionaries import *
from functions import *
import time

"""
Camilo Castro
Project script to a vocabulary enhancement game.
"""

#Run-time code
def main():
    introduction()
    #iterator for the game
    # collect information about the player
    user_collection()
    print(
    """
    
    Remember to use 'q' to quit
    ---------------------------
    
    """)
    # greet our player
    print(f' Hello {user["name"]}.')
    #sleep timer 1 seconds
    time.sleep(1)
    # round counter initializer variable.
    round = 0
    while True:
        # Round counter
        round += 1
        print(f"Player: {user.get('name')}")
        if user.get('score') == None:
            print("Score: 0")
        else:
            print(f"Score: {user.get('score')}")
        print(f"Round: {round}")
        # Call the game function
        game()
        

#Call main function
if __name__ == "__main__":
    main()
