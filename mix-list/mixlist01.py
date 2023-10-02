#!/usr/bin/env python3
"""
Camilo Castro
"""
#Run-time code
def main():
	my_list = [ "192.168.0.5", 5060, "UP" ]
	
	#Display the first item on the list
	print("The first item in the list (IP): " + my_list[0] )

	#Display the second item on the list as string
	print("The second item in the list (port): " + str(my_list[1]) )


	#Display the last item on the list.
	print("The last item in the list (state): " + my_list[2] )

    





#call the main function
if __name__ == "__main__":
	main()
