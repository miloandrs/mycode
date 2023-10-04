#!/usr/bin/env python3
"""
Camilo Castro
"""

#Run-time code
def main():
    while True:
            try:
                print("Enter a file name: ")
                name = input()
                with open(name, "w") as myfile:
                    myfile.write("No problems with that file name.")
                break
            except:
                print("Error with that file name! Try again...")

#Call main function
if __name__ == "__main__":
    main()
