#!/usr/bin/env python3

import netifaces
print(netifaces.interfaces())

for i in netifaces.interfaces():
    #attributes = vars(i)
    print('\n**************Details of Interface - ' + i + ' *********************')
    print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
    #print(dir(netifaces.ifaddresses(i)))
    #print(attributes)

