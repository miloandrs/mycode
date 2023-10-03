#!/usr/bin/env python3
# importing libraried for this code
import shutil
import os

"""
Camilo Castro | Test with of and file manipulation
"""
# Run-time code
def main():
    # forcing the program to start in specific folder
    os.chdir("/home/student/mycode/")
    #move specific object
    shutil.move('raynor.obj', 'ceph_storage/')
    # Ask the user for a new name for the "kerrigan.obj"
    xname = input("What is the new name for kerrigan.obj?")
    #move the aforementioned object with new name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
    

# Call main function
if __name__ == "__main__":
    main()
