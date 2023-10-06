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
