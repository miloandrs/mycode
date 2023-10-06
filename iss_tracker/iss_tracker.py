#!/usr/bin/python3
"""tracking the location of the ISS"""

#library imports    
import requests

## Define URL
AZIMUTH = 'http://api.open-notify.org/iss-now.json'

def main():
    """runtime code"""
    ## create the request
    stratos = requests.get(AZIMUTH)
    tower = stratos.json()
    print(f"The current location of the ISS is Latitude: {tower['iss_position']['latitude']} and Longitude: {tower['iss_position']['longitude']}")
    print('Link to google maps coming soon')


if __name__ == "__main__":
    main()

