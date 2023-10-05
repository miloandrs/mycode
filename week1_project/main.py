#!/usr/bin/env python3
import time
import dictionaries
import functions

"""
Camilo Castro
Project script to a vocabulary enhancement game.
"""
def main():
    """main function"""
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
    print(f' Hello {functions.user["name"]}.')
    #sleep timer 1 seconds
    time.sleep(1)
    # Sequence counter initializer variable.
    sequence = 0
    while True:
        # Sequenece counter
        sequence += 1
        print(f"Player: {functions.user.get('name')}")
        if functions.user.get('score') is None:
            print("Score: 0")
        else:
            print(f"Score: {functions.user.get('score')}")
        print(f"Round: {sequence}")
        # Call the game function
        functions.game()

if __name__ == "__main__":
    # Call main function
    main()
