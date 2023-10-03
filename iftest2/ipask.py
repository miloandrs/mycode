#!/usr/bin/env python3
"""
This is the introduction banner
"""


#Run-time code
def main():
    # this line now prompts the user for input
    ipchk = input("Apply an IP address: ") 
    


    if ipchk:
        print("Looks like the IP address was set: " + ipchk) # indented under if
    else:    
        print("You did not provide input.") # indented under else






#Call main function
if __name__ == "__main__":
    main()
