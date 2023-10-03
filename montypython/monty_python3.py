#!/usr/bin/env python3
import uuid
"""
This is the introduction banner
"""


#Run-time code
def counter():
    round = 0
    answer = " "
    while round < 3 and answer != "Brian":
        # increase the round counter by 1
        round += 1 
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
        # logic to check if user gave correct answer
        clean_answer = "Brian"
        if answer == clean_answer.lower():
            print("Correct!")
        elif answer == clean_answer.upper():
            print("Correct!")
        elif answer == "Brian":
            print("Correct!")
        elif answer == "shrubbery":
            print("You gave the super secret answer!")
        # logic to ensure round has not yet reached 3
        elif round == 3:    
            print("Sorry, the answer was Brian.")
        # if answer was wrong
        else:                
            print("Sorry. Try again!")


def main():
    counter()
    


#Call main function
if __name__ == "__main__":
    main()
