#!/usr/bin/env python3
"""
This is the introduction banner
"""


#Run-time code
def main():	
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
    # loop across the list vendors
    for x in vendors:
        print("The vendor is:" + x)  
    print("\nOur loop has ended.")





#Call main function
if __name__ == "__main__":
    main()
