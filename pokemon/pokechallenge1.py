#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
pokeapi = 'https://pokeapi.co/api/v2/pokemon/'



def main():
    """runtime code"""
    # Collect number form user
    pokenum = input('Pick a number between 1 and 151!\n >')
    # Create the request and assign the response to a variable. 
    pokemon = requests.get(pokeapi + pokenum).json()

    sprts = pokemon["sprites"]["front_default"]
    print(sprts)

if __name__ == "__main__":
    main()
