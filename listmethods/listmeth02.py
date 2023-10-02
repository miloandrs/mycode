#!/usr/bin/env python3
"""
Camilo Castro
"""
#Run-time code
def main():
	proto = ["ssh", "http", "https"]
	protoa = ["ssh", "http", "https"]
	print(proto)
	proto.append("dns") # this line will add "dns" to the end of our list
	protoa.append("dns") # this line will add "dns" to the end of our list
	print(proto)
	proto2 = [ 22, 80, 443, 53 ] # a list of common ports
	proto.extend(proto2) # pass proto2 as an argument to the extend method
	print(proto)
	protoa.append(proto2) # pass proto2 as an argument to the append method
	print(protoa)
	print(proto.pop(0)) #Remove first item from list
	protoa.reverse() #reverse protoa list
	print(protoa) #Print the list

	


#call the main function
if __name__ == "__main__":
	main()
