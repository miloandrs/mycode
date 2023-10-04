#!/usr/bin/env python3
from dictionaries import *
from random import choice
"""
Camilo Castro
Project script to 
"""
#global variables
fancy_word = choice(word_pool)
user_entry = " "



# function to collect user informaion
def user_collection():
    username = input("How shall we address you? \n>> ")
    user["name"] = username


# function to introduce the game
def introduction():
    #banner to introduce the game.
    intro = """
    welcome to a game of advanced vocabulary!
    your goal is to provide correct synonyms
    to the words shown. 

    remember to just have fun!
    """
    
    print(intro.upper())

# main game function
def game():
    #print statement to show the word, the indentation was intentionally left like this.    
    print(f"""
                YOUR WORD IS:
                
                {fancy_word}
                
                
                """)
    
    # collect synonym user entry
    globals()["user_entry"] = input("Think about a synonym for the aforementioned work and inter it here. \n>> ")
    # conditional to break on user input
    if user_entry == 'q':
        print("""
            
            Good Bye!
            
            """)
        exit()        
    # call the word check function
    check_word()
    

# Function to check user word
def check_word():
    # Boolean tracking variable
    result = False
    # Iterate through the list of synonyms
    
    for word in word_pool_dict[fancy_word]:
        # Compare the user entry to any of the list synonyms for the chosen word.
        if word == user_entry :
            result = True
            print(
                """

                **************
                * Correct!!! *
                **************

                
                """)

        
    if result == False:
        print("""

                *************************************
                * Not Quite! Please keep on trying. *
                *************************************
                
                
            """)













