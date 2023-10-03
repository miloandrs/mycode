#!/usr/bin/env python3
"""
This is the introduction banner
"""


#Run-time code
def main():	
    #open the file
    with open("dnsservers.txt", "r") as dnsfile:
        # indent to keep the dnsfile object open
        # loop over lines
        for svr in dnsfile:
            #print and end without a newline
            print(svr, end="")

    





#Call main function
if __name__ == "__main__":
    main()
