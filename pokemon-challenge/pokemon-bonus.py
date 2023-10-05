#!/usr/bin/env python3

import requests
import subprocess

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    pokeimg_url = (pokeapi["sprites"]["front_default"])

    subprocess.call(["curl", "-O", pokeimg_url])
main()

