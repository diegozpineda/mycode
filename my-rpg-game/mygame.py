#!/usr/bin/env python3
#
#
'''
My first rpg game
Diego Pineda
'''
#from rand import randint
import random

player_move = ''
global_dice = ''

my_main_character = {"HP": 100, "Strength": 15}

dungeon_enemies = [ 
    {"Goblin": {"HP": 20, "Strength": 5, "Name": "Goblin"}},
    {"Orc" : {"HP": 60, "Strength": 10, "Name": "Orc"}},
    {"Warrior": {"HP": 70, "Strength": 15, "Name": "Warrior"}},
    {"Cyclops": {"HP":200, "Strength": 60, "Name": "Cyclops"}}]
        

def game_dialog(dialog: str):
    # pick a dialog to print
    dash = '-'
    if dialog == 'keyboard_menu':
        print(
        '''
        Keyboard Map:
        W: UP
        A: LEFT
        S: DOWN
        D: RIGHT
        X: ATTACK
        Z: RUN
        Q: QUIT
        H: HELP
        ''')
        print(dash * 20)

    elif dialog == 'run_away':
        print(
        '''
        You have decided to run away!
        ''')
        print(dash * 20)
    elif dialog == 'player_stats':
        print(
        '''
        Here are your current stats:
        ''')
        print(my_main_character)
        print(dash * 20)
    elif dialog == 'move':
        print(
        '''
        You have decided to move! 
        ''')
        #print(my_main_character)
        print(dash * 20)
    elif dialog == 'safe':
        print(
        '''
        There is nothing in this part of the dungeon!
        ''')
        #print(my_main_character)
        print(dash * 20)
    elif dialog == 'game_start':
        print(
        '''
        Welcome to the dungeon!
        ''')
        #print(my_main_character)
        print(dash * 20)
    elif dialog == 'game_quit':
        print(
        '''
        You value your life more than adventure I see... wise choice! Remember, the dungeon will always call for you!" 
        ''')
        #print(my_main_character)
        print(dash * 20)
    elif dialog == 'game_over':
        print(
        '''
        You have died in the nether dungeon. May you celebrate with glory in the halls of valhalla with your comerades in arms! 
        ''')
        #print(my_main_character)
        print(dash * 20)

def keyboard():
    # Capture movement from keyboard
    move = input(f'Please enter a player move: > ')
    move = move.lower()

    # Define moves for keyboard
    if move == 'w':
        return 'UP'
    elif move == 'a':
        return 'LEFT'
    elif move == 's':
        return 'DOWN'
    elif move == 'd':
        return 'RIGHT'
    elif move == 'x':
        return 'ATTACK'
    elif move == 'z':
        return 'RUN'
    elif move == 'h':
        return 'HELP'
    elif move == 'q':
        return 'QUIT'
    else:
        return False

def fight(player: dict, enemy_type: dict):
    #Print Fight Dialog
    print(f'Player 1 has entered a fight with {enemy_type["Name"]}!')
    #print('Player 1 has entered a fight with ' + str(enemy_type['Name']) + "!")

    # Roll dice
    dice = random.randint(0,1)
    if dice == 0:
        # Player gets to attack first
        enemy_type["HP"] = enemy_type["HP"] - player["Strength"]
        print(f'Player attacked {enemy_type["Name"]} for {player["Strength"]} damage!')
        print(f'Enemy has {enemy_type["HP"]} HP left.')
    elif dice == 1:
        # Enemy gets to attach first
        player["HP"] = player["HP"] - enemy_type["Strength"]
        print(f'{enemy_type["Name"]} attacked Player for {enemy_type["Strength"]} damage!')
        print(f'Player has {player["HP"]} HP left.')


def spawn_enemy(enemies: list):
    # Pick a random enemy from enemy list
    rand_index = random.randint(0, 3)
    enemy_key = list(enemies[rand_index].keys())[0]
    return enemies[rand_index][enemy_key]

def roll_dice():
    # Roll dice to determine if you will encounter enemy
    dice = random.randint(0,1)
    return dice

def main():

    game_dialog('game_start')
    game_dialog('player_stats')
    game_dialog('keyboard_menu')
    player_move = keyboard()
    while player_move != 'QUIT' or my_main_character["HP"] >= 0:
        if my_main_character["HP"] <= 0:
            game_dialog('game_over')
            break
        elif player_move == 'HELP':
            game_dialog('keyboard_menu')
            player_move = keyboard()
        elif player_move == 'QUIT':
            game_dialog('game_quit')
            break
        elif player_move == 'ATTACK':
            enemy_now = spawn_enemy(dungeon_enemies)
            #test_dice = random.randint(0,3)
            #enemy_now = dungeon_enemies[test_dice]
            print(f'{enemy_now}')
            fight(my_main_character, enemy_now) 
            game_dialog('player_stats')
            player_move = keyboard()
        elif player_move == 'UP' or 'LEFT' or 'DOWN' or 'RIGHT':
            global_dice = roll_dice()
            if global_dice == 0:
                game_dialog('safe') 
            elif global_dice == 1:
                #fight(my_main_character, spawn_enemy(dungeon_enemies))
                enemy_now = spawn_enemy(dungeon_enemies)
                #test_dice = random.randint(0,3)
                #enemy_now = dungeon_enemies[test_dice]
                print(f'{enemy_now}')
                print(f'{type(enemy_now)}')
                fight(my_main_character, enemy_now) 
                game_dialog('player_stats')
            player_move = keyboard()
                
if __name__ == "__main__":
    main()


