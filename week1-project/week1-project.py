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

def main():
    intro_prompt()
    capture_network()

if __name__ == "__main__":
    main()
