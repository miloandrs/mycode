#!/usr/bin/env python3
import uuid
"""
This is the introduction banner
"""


#Run-time code
def main():
    howmany = int(input("How many UUIDs should be generated? "))
    print("Generating UUIDs...")
    # range is required because an int cannot be looped
    for rando in range(howmany):
        print( uuid.uuid4() )   # each time through the loop produce a UUID

        



#Call main function
if __name__ == "__main__":
    main()

