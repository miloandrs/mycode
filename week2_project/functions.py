#!/usr/bin/env python3
import dictionaries
from random import choice
import requests
import os
import threading
import time
import crayons
"""
Camilo Castro
Project script for a vocabulary game. 
"""

def spin():
    #Activate the server.
    #This will open server file 'game_api.py'
    if dictionaries.user.get('round') == 1:
        os.system('python3 small_project/Week2_version/game_api.py 1> /dev/null &')
        time.sleep(3)
        
        
"""VISUAL SEPARATOR"""
    
def populator():
    """function to populate dictionaries"""
    #make an api request to populate 'word_pool_dict'
    game_api = "http://127.0.0.1:2224/"
    #data
    selected_set = requests.get(game_api + dictionaries.user.get("selection")).json()
    #word list population and dictionary population
    if dictionaries.user.get("selection") == "full":
        for item in selected_set.keys():
            dictionaries.word_pool_dict.update(selected_set[item])
        dictionaries.word_pool.extend(dictionaries.word_pool_dict.keys())
    else:            
        dictionaries.word_pool = list(selected_set)    
        dictionaries.word_pool_dict = selected_set

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
    # create a thread to call spin function
    threading.Thread(target=spin, daemon=True).start()
    #wait for the server to run 5 seconds
    time.sleep(5)
    populator()
    fancy_word = choice(dictionaries.word_pool)
    #print statement to show the word, the indentation was intentionally left like this.    
    print(crayons.cyan(f"""
                YOUR WORD IS:
                
                {fancy_word}
                
                
                """))
    # collect synonym user entry
    user_entry= input("Think about a synonym for the aforementioned word and enter it here. \n>> ")
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
            print(crayons.green(
                """

                **************
                * Correct!!! *
                **************

                
                """))
            break
        else:
            result = False
    if result == False:
        print(crayons.red("""

                *************************************
                * Not Quite! Please keep on trying. *
                *************************************
                
                
            """))
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













