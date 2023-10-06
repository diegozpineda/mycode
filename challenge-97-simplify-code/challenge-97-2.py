#!/usr/bin/env python3
 
zodiac = {
    "Rabbit": "vigilant, witty, quick-minded, and ingenious."
    "Rat": "artistic, sociable, industrious, charming, and intelligent."
    "Tiger": "courageous, enthusiastic, confident, charismatic, and a leader."
    "Ox": "strong, thorough, determined, loyal, and reliable."
    "Dragon": "talented, powerful, lucky, and successfull."
    "Snake": "wise, like to work alone, and determined."
    "Horse": "animated, active, and energetic."
    "Sheep": "creative, resilient, gentle, mild-mannered, and shy."
    "Monkey":"sharp, smart, curious, and mischievious."
    "Rooster":"hardworking, resourceful, courageous, and talented."
    "Dog": "loyal, honest, cautious, and kind."
    "Pig":"symbol of wealth, honesty, and practicality." }


def main():    
    usr_name = input("Please enter your name:\n>") 
              
    usr_name = usr_name.title()    
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
            
    if usr_date in [2011, 1999, 1987, 1975, 1963]:
        print(f"{usr_name} your zodiac sign is Rabbit, you are {zodiac['Rabbit']}") 
    elif usr_date in [2020, 2008, 1996, 1984, 1972, 1960]:
        print(f"{usr_name} your zodiac sign is Rat, you are {zodiac['Rat']}") 
    elif usr_date in [2010, 1998, 1986, 1974, 1962]:
        print(f"{usr_name} your zodiac sign is Tiger, you are {zodiac['Tiger']}")  
    elif usr_date in [2021, 2009, 1997, 1985, 1973, 1961]:
        print(f"{user_name} your zodiac sign is Ox, you are {zodiac['Ox']}")  
    elif usr_data in [2012, 2000, 1988, 1976, 1964]:    
        print(f"{usr_name} your zodiac sign is Dragon, you are {zodiac['Dragon']}")  
    elif usr_date in [2013, 2001, 1989, 1977, 1965]:
        print(f"{usr_name} your zodiac sign is Snake, you are {zodiac['Snake']}")  
    elif usr_date in [2014, 2002, 1990, 1978, 1966]:
        print(f"{usr_name} your zodiac sign is Horse, you are {zodiac['Horse']}")  
    elif usr_date in [2015, 2003, 1991, 1979, 1967]:
        print(f"{usr_name} your zodiac sign is Sheep, you are {zodiac['Sheep']}")  
    elif usr_date in [2016, 2004, 1992, 1980, 1968]:
        print(f"{usr_name} your zodiac sign is Monkey, you are {zodiac['Monkey']}")  
    elif usr_date in [2017, 2005, 1993, 1981, 1969]:
        print(f"{usr_name} your zodiac sign is Rooster, you are {zodiac['Rooster']}")  
    elif usr_date in [2018, 2006, 1994, 1982, 1970]:
        print(f"{usr_name} your zodiac sign is Dog, you are {zodiac['Dog']}")  
    elif usr_date in [2019, 2007, 1995, 1983, 1971]:
        print(f"{usr_name} your zodiac sign is Pig, you are {zodiac['Pig']}")  

if __name__ == "__main__":
    main()

