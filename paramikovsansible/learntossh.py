#!/usr/bin/python3

# standard library
import os

# 3rd party imports
import paramiko     # paramiko is a "pure-python" SSH solution
                    # that is to say, you don't need other SSH libraries to use it

# shortcut issuing commands to remote
def commandissue(command_to_issue, sshsession):
    """when sshsession.exec_command is issued, it returns a 3-tuple, we are
       only interested in standard out, which is what this function returns"""
    
    # issue command and return 3-touple
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read() # return the standard out

def main():
    """sending commands across an SSH channel"""
    
    # create an SSH session (this is like opening PuTTY and selecting "ssh")
    sshsession = paramiko.SSHClient()

    ############# IF YOU WANT TO CONNECT USING UN/PW ################
    #sshsession.connect(server, username=username, password=password)
    ############## IF USING KEYS ####################################

    # mykey is our private key
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # if we never went to this SSH host
    # auto add the fingerprint to the known host file (otherwise the script will hang)
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # creds to connect (to a single host)
    sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

    # a simple list of commands to issue across our connection
    our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

    # cycle through our commands and issue them on the far end
    for x in our_commands:
        print(commandissue(x, sshsession).decode('utf-8'))

    # close the connection
    sshsession.close()
    
# call our main function
if __name__ == "__main__":
    main()

