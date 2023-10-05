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
    #collect the setcode
    setcode = input("Please enter the card setcode you would like to see(See the set index for reference on codes)")

    #create rsp which is the requested object
    rsp = requests.get(f"{API}cards?sets={setcode}")
    
    # The .json() method will create a python dictionary which is easier than using urllib
    #pull full into variable    
    cards = rsp.json()
    # display output
    print(cards)

if __name__ == "__main__":
    # call in the main function
    main()
