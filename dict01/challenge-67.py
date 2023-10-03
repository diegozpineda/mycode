#!/usr/bin/env python3
#
#
#char_name = input(f'Which character do you want to know about? (Starlord, Mytique, Hulk)')
#char_stat = input(f'What statistic do you want to know about? (real name, powers, archenemy)')

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
}


#def return_char_name(hero: str):
#    return marvelchars[hero]


#def return_char_stat(stat: str):
#    return marvelchars[hero][stat]

def main():
    char_name = input(f'Which character do you want to know about? (Starlord, Mytique, Hulk)')
    char_stat = input(f'What statistic do you want to know about? (real name, powers, archenemy)')

    #return_char_name(char_name)
    #return_char_stat(char_stat)
    print(f'{marvelchars[char_name]["real name"]}s {char_stat} is :  {marvelchars[char_name][char_stat]}') 

if __name__ == "__main__":
    main()
