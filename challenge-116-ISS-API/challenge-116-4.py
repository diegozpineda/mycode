#!/usr/bin/env python3
'''
Obtain data from NASA ISS tracker
Diego Pineda
'''

import requests
import datetime
import reverse_geocoder as rg

#import json

def main():

    apiurl = 'http://api.open-notify.org/iss-now.json'

    issdata = requests.get(apiurl)

    issjson = issdata.json()
    coords_tuple = (issjson["iss_position"]["latitude"], issjson["iss_position"]["longitude"]) 
    result = rg.search(coords_tuple, verbose=False)
    city = result[0]['name']
    country = result[0]['cc']

    #print(issjson)
    print('Current Location of the ISS:\n')
    print(f'Lon: {issjson["iss_position"]["longitude"]}\n')
    print(f'Lat: {issjson["iss_position"]["latitude"]}\n')
    print(f'Timestamp: {datetime.datetime.fromtimestamp(issjson["timestamp"])}')
    print(f'City: {city}')
    print(f'Country: {country}')
    #print(result)

if __name__ == "__main__":
    main()
