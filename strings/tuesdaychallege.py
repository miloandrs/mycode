#!/usr/bin/env python3
"""
Fixed by Camilo Castro
"""


def main():
	#Run-time code

	mylist = [1,2,3,4,5, "Python"]

	name = input("What is your name?\n>")

	# This is what you should see when print runs-
	# Hi <name>! Welcome to Day 2 of Python Training!
	print("Hi " + name.title() + "! Welcome to Day " + str(mylist[1]) + " of " + mylist[5] + " Training!")







#call the main function
main()
