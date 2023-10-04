#!/usr/bin/env python3
#
#
''' review of try and except logic | alta3 research '''

while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    except:
        print("ERROR! File name invalid. Pls try again...")
