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
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

# user will never roll anything lower than a 3
class Cheat_High_Roller(Player):
    def cheat(self):
        self.dice = []
        for i in range(3):
            self.dice.append(randint(3,6))

# user will roll a 6 about 50% of the time
class Cheat_Fifty(Player):
    def cheat(self):
        self.dice = []
        for i in range(3):
            if randint(0,1) == 0:
                roll = 6
            else:
                roll = randint(1,6)
            self.dice.append(roll)

# user will reroll if dice sum is less than 9
class Cheat_Mulligan(Player):
    def cheat(self):
        if sum(self.dice) < 9:
            self.dice = []
            for i in range(3):
                self.dice.append(randint(1,6))

# user will add a die roll
class Cheat_Add(Player):
    def cheat(self):
        self.dice.append(randint(1,6))

# User will make the opponents roll poorly
class Cheat_Sabotage(Player):
    def cheat(self, other):
        other.dice = []
        for i in range(3):
            other.dice.append(randint(1,3))