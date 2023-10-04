#!/usr/bin/env python3
"""
Camilo Castro
"""


#Run-time code
def main():
    #Open the file 
    vampire_counts = 0
    with open("dracula.txt", "r") as boo:
        with open("draculas.txt", "w") as moo:
            for line in boo:
                if "vampire" in line.lower():
                    vampire_counts += 1
                    moo.write(line)
                    print(line)


    print(f'The vampiric times are: {vampire_counts}')


#Call main function
if __name__ == "__main__":
    main()
