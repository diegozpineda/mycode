#!/usr/bin/env python3
#
#
#print(__name__)
#print("Module #1 Name=", __name__)

print("This code will always execute.")

def main():
    #print("Module #1 Name=", __name__)
    print(f'This code belongs to the main function in module 1.')

if __name__ == "__main__":
    main()
    #print("Code is being run directly from Python.")
#else:
    #print("Code is being run indirectly from import.")
