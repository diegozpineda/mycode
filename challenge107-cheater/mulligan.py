#!/usr/bin/env python3
'''
mulligan
challenge 107
Diego Pineda
'''

from random import randint
from cheatdice import Player

class Mulligan(Player): #inheritence of player
    def cheat(self):
        if len(self.dice) == 3 and sum(self.get_dice()) < 9:
            self.roll()

