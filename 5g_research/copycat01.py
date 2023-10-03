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
    # copying an existing file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    # copying the whole folder
    shutil.copytree("5g_research/", "5g_research_backup/")



# Call main function
if __name__ == "__main__":
    main()
