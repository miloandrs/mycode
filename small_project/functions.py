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



def introduction():
    #banner to introduce the game.
    intro = """
    welcome to a game of advanced vocabulary!
    your goal is to provide correct synonyms
    to the words shown. 

    remember to just have fun!
    """
    
    print(intro.upper())

def game():
    #print statement to show the word, the indentation was intentionally left like this.    
    print(f"""
                YOUR WORD IS:
                
                {fancy_word}
                
                
                """)
    
    # collect synonym user entry
    globals()["user_entry"] = input("Think about a synonym for the aforementioned work and inter it here. \n>> ") 
    # call the word check function
    check_word()
    
    
def check_word():
    # Iterate through the list of synonyms
    for word in word_pool_dict[fancy_word]:
        result = 0
        # Compare the user entry to any of the list synonyms for the chosen word.
        if word == user_entry :
            result = 1
            print("""
        
    **************
    * Correct!!! *
    **************

        
        """)      
        
    if result == 0:
        print("""
        
    *************************************
    * Not Quite! Please keen on trying. *
    *************************************

        
        """)













