#!/usr/bin/env python3
import time
import functions
import dictionaries

"""
Camilo Castro
Project script to a vocabulary enhancement game.
"""
def main():
    """runtime code"""
    functions.introduction()
    #iterator for the game
    # collect information about the player
    functions.user_collection()
    print(
    """
    
    Remember to use 'q' to quit
    ---------------------------
    
    """)
    # greet our player
    print(f' Hello {dictionaries.user["name"]}.')
    #sleep timer 1 seconds
    time.sleep(1)
    # Sequence counter initializer variable.
    sequence = 0
    while True:
        # Sequenece counter
        sequence += 1
        print(f"Player: {dictionaries.user.get('name')}")
        if dictionaries.user.get('score') is None:
            print("Score: 0")
        else:
            print(f"Score: {dictionaries.user.get('score')}")
        print(f"Round: {sequence}")
        # Call the game function
        functions.game()

if __name__ == "__main__":
    # Call main function
    main()
