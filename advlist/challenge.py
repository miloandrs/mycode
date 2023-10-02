#!/usr/bin/env python3
"""
Camilo Castro
"""
#Run-time code
def main():
	#Create animal list
	animal_list = ["Dog", "Cat", "Fox", ["Bee", "Fly"]]

	#display the last nested list
	print(animal_list[3])

	#display fly
	print(animal_list[3][1])


	#pop the nested list into another list
	bee_list = animal_list.pop(3)

	#print the new list

	print(bee_list)


	#concatenate both lists
	long_list = animal_list + bee_list

	#print the new list
	print(long_list)


	


#call the main function
if __name__ == "__main__":
	main()
