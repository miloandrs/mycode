#!/usr/bin/env/python3
"""
Camilo Castro
nasa API usage
"""

#imports
import urllib.request
import json

# define the nada api link
nasa_api = "https://api.nasa.gov/planetary/apod?"

def main():
    """ runtime code"""
    #open and initialize the creds into a variable.
    with open('nasa.creds') as mycreds:
        nasacreds = mycreds.read()

    #remove the new line from txt files
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ## Call the webservice with our key
    apodurlobj = urllib.request.urlopen(nasa_api + nasacreds)

    ## read the file-like object
    apodread = apodurlobj.read()

    ## decode JSON to Python data structure
    apod = json.loads(apodread.decode("utf-8"))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])
if __name__ == "__main__":
    main()
