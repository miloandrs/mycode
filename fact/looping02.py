#!/usr/bin/env python3
"""
This is the introduction banner
"""


#Run-time code
def main():	
    #open the file
    dnsfile = open("dnsservers.txt", "r")

    #create a list of lines
    dnslist = dnsfile.readlines()


    #loop over the lines
    for svr in dnslist:
        print(svr, end="")
    
    dnsfile.close()
    
    





#Call main function
if __name__ == "__main__":
    main()
