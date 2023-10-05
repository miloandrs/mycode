#!/usr/bin/env python3
import crayons
import json
"""
Camilo Castro
"""

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.yellow("Handshaking")} . .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# function to reboot devices
def devicereboot():
    with open("ip_list.txt", "r") as ip_list:
        for line in ip_list.readlines():
            print(f"{crayons.blue('Connecting...')}")
            print(f"{crayons.red('REBOTTING')}")
            






#Run-time code
def main():    
    """called at runtime"""
    # open json file
    with open('devicecmd.json', 'r') as devicecmdfile:
        devicecmd = json.load(devicecmdfile)


    """ unused code delimiter line """
    # dict containing IPs mapped to a list of physical interfaces and their state
    #devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    #["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    """ unused code delimiter line """



    print(f"Welcome to the {crayons.green('network')} device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    devicereboot()

    



#Call main function
if __name__ == "__main__":
    main()
