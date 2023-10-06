#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random

URL= "https://opentdb.com/api.php?amount=10&category=23&difficulty=medium&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    n = 0
    for i in data["results"]:
        questions = []
        n = 0
        print(f'Question: {i["question"]}') 
        #questions.append(i["correct_answer"]
        for j in i["incorrect_answers"]:
            questions.append(j)
        questions.append(i["correct_answer"])
        counter = 1
        for k in questions:
            #counter = 1
            print(f'{counter}. {k}')
            counter += 1
        

if __name__ == "__main__":
    main()

