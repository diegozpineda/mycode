#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Player - Class model
   Cheat_Swapper(Player) - Subclass model
   Cheat_Loaded_Dice(Player) - Subclass model"""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = []
        for i in range(3):
            self.dice.append(randint(1,6))

    def get_dice(self):
        return self.dice

class Cheat_Swapper(Player): #inheritence of player
    def cheat(self):
        self.dice[2] = 6
        # self.dice[-1] = 6
        # i.e. set last dice to 6 (i.e. this guy cheating)

class Cheat_Loaded_Dice(Player): #inheritence of player
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

class Mulligan(Player): #inheritence of player
    def cheat(self):
        if len(self.dice) == 3 and sum(self.get_dice()) < 9:
            self.roll()

class Add_Die(Player): #inheritence of player
    def cheat(self):
        self.dice.append(randint(1,6))
        return None

class Weighted_Die(Player): #inheritence of player
    def cheat(self):
        # must start with first die, i.e self.dice[0]
        self.dice = []
        self.dice.append(randint(1,6))

    def roll_2(self):
        # need a new roll function that will not overwrite the first dice roll
        for i in range(2):
            self.dice.append(randint(1,6))

#class Sabotage(Player, Player
