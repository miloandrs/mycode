#!/usr/bin/env python3
"""
Camilo Castro | Moving files with sftp
"""
#imports
import paramiko #importing so we can do SSH
import os #importing standard library to interact with the OS
import getpass
#Run-time code
def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    ## copy our firstpasswd.py script to bender
    sftp.put("file_to_move.txt", "file_to_move.txt") # move file to target location home directory
    
    ## close the connection
    sftp.close() # close the connection

#Call main function
if __name__ == "__main__":
    main()
