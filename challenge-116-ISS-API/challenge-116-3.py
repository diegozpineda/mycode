#!/usr/bin/env python3
'''
Obtain data from NASA ISS tracker
Diego Pineda
'''

import requests
import datetime

#import json

def main():

    apiurl = 'http://api.open-notify.org/iss-now.json'

    issdata = requests.get(apiurl)

    issjson = issdata.json()

    #print(issjson)
    print('Current Location of the ISS:\n')
    print(f'Lon: {issjson["iss_position"]["longitude"]}\n')
    print(f'Lat: {issjson["iss_position"]["latitude"]}\n')
    print(f'Timestamp: "{datetime.datetime.fromtimestamp(issjson["timestamp"])}')

if __name__ == "__main__":
    main()
