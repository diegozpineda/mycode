#!/usr/bin/env python3
#
#
'''
Goal of this project is to provide a network address and to provide
Basic information regarding the network address
'''

import ipaddress

def intro_prompt(): 
    #Prommpt for input and define format
    print(f'Please enter an IPv4 Network in one of the following formats below:')
    print(f'1. 192.168.1.0/24')
    print(f'1. 192.168.1.0/255.255.255.0')
    print(f'1. 192.168.1.0/0.0.0.255')

def capture_network():
    #Capture input
    user_input = input(f'>: ')

    while ipaddress.IPv4Network(user_input) == False:
        print(f'You did not enter a valid IPv4 network, please try again')
        intro_prompt()
        user_input = input(f'>: ')

    return ipaddress.IPv4Network(user_input)

#def get_network_address(network):
#    
#    return 
#
#def get_broadcast_address(network):
#
#def get_netmask_address(network):
#
#def get_number_hosts(network):
#
#def get_prefix_len(network):

def get_info(network: object): 
    # Initialize New Dictionary
    netinfo = {}

    #Populate using builtin network object methods
    netinfo["network_address"] = network.network_address
    netinfo["broadcast_address"] = network.broadcast_address
    netinfo["hostmask"] = network.hostmask
    netinfo["netmask"] = network.netmask
    netinfo["prefixlen"] = network.prefixlen
    netinfo["hosts"] = network.num_addresses

    return netinfo

#def net_info_keys(netinfo:dict,

def print_netinfo(netinfo: dict):
    # print a few newlines to nicely format output
    delimiter = '-'
    print(f'\n')
    print(delimiter * 20)
    print(f'\n')

    # print key and value pairs by enumerating items
    for  i, (k, v) in enumerate(netinfo.items()):
        print(f'{k}: {v}')

def main():
    intro_prompt()
    my_network = capture_network()
    my_network_info = get_info(my_network)
    #print(my_network_info)
    print_netinfo(my_network_info)

if __name__ == "__main__":
    main()
