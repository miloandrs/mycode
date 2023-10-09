"""Alta3 Research | RZFeeser
   Using netmiko to connect to many different devices to issue 'show arp' """

# standard library
from datetime import datetime

# python3 -m pip install netmiko
from netmiko import ConnectHandler 

# dictionary of connection info for
# cisco endpoint
#cisco3 = {
#    'device_type': 'cisco_ios',
#    'host':   'cisco3.example.com',
#    'username': 'admin',
#    'password': 'cisco123',
#    }
    
#cisco_asa = {
#    'device_type': 'cisco_asa',
#    'host': '10.10.10.88',
#    'username': 'admin',
#    'password': 'cisco123',
#    'secret': 'cisco123',
#    }

#cisco_xrv = {
#    'device_type': 'cisco_xr', 
#    'host': '10.10.10.77', 
#    'username': 'admin', 
#    'password': 'cisco123', 
#    }

arista1 = { 
    'device_type': 'arista_eos', 
    'host':   'sw-1', 
    'username': 'admin', 
    'password': 'alta3', 
    } 

arista2 = { 
    'device_type': 'arista_eos', 
    'host':   'sw-2', 
    'username': 'admin', 
    'password': 'alta3', 
    } 

#hp_procurve = { 
#    'device_type': 'hp_procurve', 
#    'host': '10.10.10.68', 
#    'username': 'admin', 
#    'password': '!cisco123', 
#    } 

#juniper_srx = { 
#    'device_type': 'juniper', 
#    'host':   'srx1.domain.com', 
#    'username': 'admin', 
#    'password': '!cisco123', 
#    } 


# make a list containing all of the login information we declared
#all_devices = [cisco3, cisco_asa, cisco_xrv, arista8, hp_procurve, juniper_srx]

# we only have 2 switches so we'll create a 
# list containing only our "real" connection
# information
all_devices = [arista1, arista2]

# when our script begins, get the start time
start_time = datetime.now() 

# loop across the dictionaries
for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)  # unpack the dictionary
    output = net_connect.send_command("show arp")  # this is the command to issue
    
    # window dressing shwoing the results
    print(f"\n\n--------- Device {a_device['device_type']} ---------") 
    print(output) 
    print("--------- End ---------") 
  
# get the stop time
end_time = datetime.now()

# display the total time it took
total_time = end_time - start_time
print(f"Finished in {total_time} seconds")

