#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=10&category=23&difficulty=medium&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    n = 0
    for i in data["results"]:
        print(f'Question: {i["question"]}') 
        print(f'Question: {i["correct_answer"]}\n') 

if __name__ == "__main__":
    main()

