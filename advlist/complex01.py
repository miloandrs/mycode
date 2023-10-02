#!/usr/bin/env python3
"""
Camilo Castro
"""
#Run-time code
def main():
	# create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    #display second item in the list
    print(list1[1])

    #Add second list 
    list2 = ["Juniper"]

    #Extend list1 with list2
    list1.extend(list2)


    #Print the extended list1
    print(list1)

    # create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    
    # use the append operation to append list1 by list3
    list1.append(list3)
    
    # display the new complex list1
    print(list1)

    # display the list of IP addresses
    print(list1[4])

     # display the first item in the list (0th item) - first IP address
    print(list1[4][0])
	

	


#call the main function
if __name__ == "__main__":
	main()
