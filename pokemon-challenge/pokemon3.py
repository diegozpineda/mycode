#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    #print(pokeapi["sprites"]["front_default"])

    # Part3 - determine number of games pokemon is in 
    # dictionary nested inside a list
    # second element
    num_games = 0
    for i in pokeapi["game_indices"]:
        num_games += 1 
        #print(f'{i["move"]["name"]}')

    print(f'Total number of games pokemon is in: {num_games}')
main()

