#!/usr/bin/env python3
import uuid
"""
This is the introduction banner
"""


#Run-time code
def counter():
    #Counter variable
    round = 0
    #round iteration loop
    while True:
        round += 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess--> ")
        #answer conditional
        if answer == 'Brian':
            print('correct')
            break
        elif round == 3:
            print('Sorry, the answer was Brian.')
            break
        else:
            print('Sorry, try again!')

def main():
    counter()
    


#Call main function
if __name__ == "__main__":
    main()
