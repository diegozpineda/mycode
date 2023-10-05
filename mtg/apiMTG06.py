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

    # create our request object
    #resp = requests.get("https://api.magicthegathering.io/v1/sets")
    resp = requests.get(f'{API}sets')

    # display the methods available to our new object
    cardsets = (resp.json().get("sets"))
    
    # create a file to write our cardsets data into
    with open("mtgsets.index", "w") as mtgfile:
        for card in cardsets: # iterate through all cards in sets key
            print(f'{card.get("name")} -- {card.get("code")}', file=mtgfile)

if __name__ == "__main__":
    main()
