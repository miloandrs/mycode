#!/usr/bin/env python3
"""
Camilo Castro
"""
#Run-time code
def main():
	proto = ["ssh", "http", "https"]
	print(proto)
	print(proto[1])
	proto.extend("dns")
	print(proto)

	


#call the main function
if __name__ == "__main__":
	main()
