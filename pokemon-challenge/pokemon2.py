#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    #print(pokeapi["sprites"]["front_default"])

    # Part2 - print all moves in moves key
    # dictionary nested inside a list
    for i in pokeapi["moves"]:
        print(f'{i["move"]["name"]}')

main()

