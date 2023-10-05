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
    
    # display the methods available to this new requested object
    print(rsp.json())    

if __name__ == "__main__":
    # call in the main function
    main()
