#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import json
import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {crayons.blue(mycmds)}')
            # we'll learn to write code that sends cmds to device here
    return None

def device_reboot(devicecmd: dict):
    for ip in devicecmd.keys(): # iterate through the keys in dict
        print(f'Connecting to ... {crayons.blue(ip)}')
        print(f'... {crayons.red("Reloading now!")}')

    return None

# start our main script
def main():
    """called at runtime"""

    # This time we will read in a json file which contains similar data structure of device
    # ip's as well as associated device interface and device cmd
    # file is read via json module
    
    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile)

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

    ## device reboot
    print(f'\n\nInitiating device reload')
    device_reboot(devicecmd)

# call our main function
main()

