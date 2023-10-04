#!/usr/bin/env python3
''' try except else and finally | alta3 research'''

#uuid library
import uuid

# gen uuid based on host id, seq number, and current time
# simulate a ticket number
ticket = uuid.uuid1()

try:
    print('Type the name of the configuration file to load.')
    configfile = input('Filename: ')
    with open(configfile, 'r') as configfileobj:
        switchconfig = configfileobj.read()
# if any errors occured        
except: 
    x = 'General error with obtaining config file!'
# if no errors
else:
    x = 'Switch config found.'
# always write output to log file, regadless of except or else
finally:
    with open("try04.log", "a") as zlog:
        print("\n\nWriting results to log file")
        print(ticket, " - ", x, file=zlog)
