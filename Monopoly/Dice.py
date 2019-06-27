"""
Class that ceates and rolls a dice
"""

import random

class Dice:

    def roll():
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return [die1, die2]
