#!/usr/bin/env python3
"""
Camilo Castro | Exploring the interfaces library
"""
#imports
import netifaces

#Run-time code
def main():
    """runtime code"""
    print(netifaces.interfaces()) #print details of all interfaces
    for i in netifaces.interfaces():
        print('\n********Details of Interface - ' + i + ' ************')
        try:
            print('MAC: ', end='') # This print statement will always print MAC without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message

#Call main function
if __name__ == "__main__":
    main()
