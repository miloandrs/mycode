#!/usr/bin/env python3
import time
import functions
import dictionaries
import pyfiglet
import crayons
import os

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
    greet = pyfiglet.figlet_format(f'Hello {dictionaries.user["name"]}!', font = "banner4")
    print(crayons.yellow(greet))
    #sleep timer 1 seconds
    time.sleep(1)
    # Sequence counter initializer variable.
    sequence = 0
    while True:
        # Sequenece counter
        sequence += 1
        dictionaries.user["round"] = sequence
        print(f"Round: {dictionaries.user.get('round')}")
        print(f"Player: {dictionaries.user.get('name')}")
        if dictionaries.user.get('score') is None:
            print("Score: 0")
        else:
            print(f"Score: {dictionaries.user.get('score')}")
        #letter input selection
        print(crayons.yellow("""

                Enter full for all of the available words
                Enter A for words that start with A
                Enter B for words that start with B
                Enter C for words that start with C
                Enter D for words that start with D
                
                """))
        selection = input("Select a dictionary: ")
    
        while True:
            if selection.upper() in ["full", "A", "B", "C", "D"]:
                dictionaries.user['selection'] = selection
                break
            elif selection == 'q':
                # Address the player
                print("""
                    
                    Good Bye!
                    
                    """)
                #kill the server
                os.system('pkill -9 -f game_api.py')
                #Close the program
                exit()        
            else:
                print("You did not enter a valid letter!")
                print("Please enter the letter of an available dictionary")
                selection = input("Select a dictionary: ")
        
        
        # Call the game function
        functions.game()

if __name__ == "__main__":
    # Call main function
    main()
