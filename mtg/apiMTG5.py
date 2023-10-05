#!/usr/bin/env python3
"""Camilo Castro

    Description:
    A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# Import the requests library
import requests

# Simplify the use of the base API into a variable. The base API never changes
API = "https://api.magicthegathering.io/v1/" 

def main():
    """Run time code"""
    #create rsp which is the requested object
    rsp = requests.get(f"{API}sets")
    
    # The .json() method will create a python dictionary which is easier than using urllib
    #get the response into a dictionary 
    cardsets = rsp.json().get("sets")

    # Loop through the dictionary os sets
    for cardset in cardsets:
        # each key is a set of cards.
        print(cardset) 

if __name__ == "__main__":
    # call in the main function
    main()
