#!/usr/bin/env python3
"""Camilo Castro

    Description:
    A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# Import the requests library
import requests

def main():
    """Run time code"""
    #create rsp which is the requested object
    rsp = requests.get("https://api.magicthegathering.io/v1/sets")
    
    # display the methods available to this new requested object
    print(dir(rsp))    

if __name__ == "__main__":
    # call in the main function
    main()
