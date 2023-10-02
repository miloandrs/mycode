#!/usr/bin/env python3
"""
Camilo Castro
"""
#Run-time code
def main():
	wordbank= ["indentation", "spaces"]
	tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
	wordbank.append(4)
	num = int(input("Please enter a number between 0 and 20:\n>"))
	student_name = tlgstudents[num]
	print(tlgstudents[num], "always uses", wordbank[2], wordbank[1], "to indent")


#call the main function
if __name__ == "__main__":
	main()
