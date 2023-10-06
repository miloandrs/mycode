#!/usr/bin/env python3
import dictionaries
from random import choice
import json
import sys
"""
Camilo Castro
Project script for a vocabulary game. 
"""

def populator():
    """function to populate dictionaries"""
    #open and populate word file
    with open('small_project/word_pool.txt', 'r') as wp:
        for line in wp:
            dictionaries.word_pool.append(line.strip(' \n'))
    #open word_pool_dict file 
    with open('small_project/jsondict.json') as wpc:
        dictionaries.word_pool_dict = json.load(wpc)
    

"""VISUAL SEPARATOR"""

def user_collection():
    """Function to collect player information"""
    username = input("How shall we address you? \n>> ")
    dictionaries.user["name"] = username

"""VISUAL SEPARATOR"""

# function to introduce the game
def introduction():
    """function to introduce the game"""
    #banner to introduce the game.
    intro = """
    welcome to a game of advanced vocabulary!
    your goal is to provide correct synonyms
    to the words shown. 

    remember to just have fun!
    """
    
    print(intro.upper())

"""VISUAL SEPARATOR"""

def game():
    """Main game function"""
    # declare global scope variables.
    global user_entry
    global fancy_word
    #call dictionary populator function
    populator()
    fancy_word = choice(dictionaries.word_pool)
    #print statement to show the word, the indentation was intentionally left like this.    
    print(f"""
                YOUR WORD IS:
                
                {fancy_word}
                
                
                """)
    # collect synonym user entry
    globals()["user_entry"] = input("Think about a synonym for the aforementioned work and inter it here. \n>> ")
    # conditional to break on user input
    if user_entry == 'q':
        # Address the player 
        print("""
            
            Good Bye!
            
            """)
        #Close the program
        sys.exit()        
    # call the word check function
    check_word()

"""VISUAL SEPARATOR"""

def check_word():
    """Function to check user word"""
    # Boolean tracking variable
    global result
    # Iterate through the list of synonyms
    for word in dictionaries.word_pool_dict[fancy_word]:
        # Compare the user entry to any of the list synonyms for the chosen word.
        if word == user_entry :
            result = True
            print(
                """

                **************
                * Correct!!! *
                **************

                
                """)
            break
        else:
            result = False
    if result == False:
        print("""

                *************************************
                * Not Quite! Please keep on trying. *
                *************************************
                
                
            """)
    #call the scoring function
    scores()

"""VISUAL SEPARATOR"""

def scores():
    """Score calculator function"""
    # condition to define score variable
    score = dictionaries.user.get('score')
    if score is None:
        score = 0
    else:
        score = int(dictionaries.user.get('score'))
    if result == True:
        score = score + 10
    dictionaries.user["score"] = score













