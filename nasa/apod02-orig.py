#!/usr/bin/env python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# fun to grab our creds
def returncreds():
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters
    nasacreds = "api_key=" + nasacreds.strip("\n")

def main():
    nasacreds = returncreds()

    apodresp = requests.get(NASAAPI + nasacreds)

    # strip json

    apod = apodresp.json()
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()
