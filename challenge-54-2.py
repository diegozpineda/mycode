#!/usr/bin/env python3
#
#
"""
Challenge 54, version 2
Diego Pineda
"""

def record_name():
    try: 
        user_name = input("What is your name?: ")

    except ValueError:
        print("Please enter a valid string.")

    return user_name

def record_day():
    try:
        week_day = str(input("what is the current day of the week?: "))

    except ValueError:
        print("Please enter a valid string.")
    
    return week_day

def validate_day(day: str):
    valid_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    for i in valid_days:
        if day == i:
            return True
        else: 
            print(f'Please enter a day in the following format: ')
            for correct_day in valid_days:
                print(f'{correct_day}, ')
            return False


if __name__ == "__main__":
    name = record_name()
    weekday = record_day()
    while validate_day(weekday) == False:
        weekday = record_day()
    print(f'Hello, {name}! Happy {weekday}!')
