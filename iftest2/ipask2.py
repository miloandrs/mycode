#!/usr/bin/env python3
"""
This is the introduction banner
"""


#Run-time code
def main():
    # this line now prompts the user for input
    ipchk = input("Apply an IP address: ")
    
    if ipchk == "192.168.70.1":
        print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
    elif ipchk: # if any data is provided, this will test true
        print("Looks like the IP address was set: " + ipchk) # indented under if
    else: # if data is NOT provided
        print("You did not provide input.") # indented under else







#Call main function
if __name__ == "__main__":
    main()
~                             
