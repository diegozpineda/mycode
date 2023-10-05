#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

# define base API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():
    '''Run time code'''

    # ask for set code to lookup on magic mtg api
    setcode = input(f'What is the code of the set you are looking up? (See mtgsets.index): ').lower()
    # create our request object
    #resp = requests.get("https://api.magicthegathering.io/v1/sets")
    resp = requests.get(f'{API}sets')

    cards = resp.json()

    # display the methods available to our new object
    #print(resp.json().keys())
    print(cards)

if __name__ == "__main__":
    main()
