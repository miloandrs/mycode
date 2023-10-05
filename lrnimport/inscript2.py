#!/usr/bin/env python3

import subprocess
"""
Camilo Castro
"""
#Run-time code
def main():
    #Use the imported library
    subprocess.call(["ip", "link", "show", "up"])
    print("This program will check your interfaces")
    interface = input("Enter and Interface in the format of 'ens3': ")
    subprocess.call(["ip", "route", "show", "dev", interface])
    subprocess.call(["ip", "route", "show", "dev", interface])



    



#Call main function
if __name__ == "__main__":
    main()
