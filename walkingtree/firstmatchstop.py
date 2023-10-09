#!/usr/bin/env python3
"""Script to seach and stop on first match"""

# imports
import os

#Define the searching funciton
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
def main():
    """Runtime code"""
    #Ask the user for file name and path
    lookfor = input('What file you need to find? \n >> ')
    lookWhere = input('Provide the path where I should be looking')
    

    #print the location
    print(find(lookfor, lookWhere))


if __name__ == '__main__':
    #Call main function
    main()
