#!/usr/bin/env python3
"""
Camilo Castro 
"""
#Run-time code
def main():
    #parse keytstone file to check for failed logins
    #Failed attempts counter
    login_fails = 0
    #open the file
    keystone_file = open('keystone.common.wsgi', 'r')
    #loop over the lines
    for line in keystone_file:
        #Condition for specific pattern in the lines
        if "- - - - -] Authorization failed" in line:
            # update the counter variable
            login_fails += 1
    print(f'The number of failed logins is {login_fails}')
    keystone_file.close()


#Call main function
if __name__ == "__main__":
    main()
