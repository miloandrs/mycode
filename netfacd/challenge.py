#!/usr/bin/env python3
"""
Camilo Castro | Exploring the interfaces library
"""
#imports
import netifaces


def find_ip(interface_name):
    """fucntion to find the ip"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_INET])[0]['addr']     # the IP address

def find_mac(interface_name):
    """fucntion to find the ip"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_LINK])[0]['addr']     # the MAC address



#Run-time code
def main():
    """runtime code"""
    print(netifaces.interfaces()) #print details of all interfaces
    for i in netifaces.interfaces():
        print('\n********Details of Interface - ' + i + ' ************')
        try:
            print('MAC:', find_mac(i)) # display MAC address information for adapter
            print('IP:', find_ip(i))   # display IP address information for adapter
        
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message

#Call main function
if __name__ == "__main__":
    main()
