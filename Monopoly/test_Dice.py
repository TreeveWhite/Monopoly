"""
Unit Test for Dice.py
"""

from Dice import Dice
import unittest
class MyTest(unittest.TestCase):
    def test_DiceRoll(self):
        result = Dice.roll()
        self.assertIn(result[0], [1,2,3,4,5,6,7,8,9,10,11,12])
        self.assertIn(result[1], [1,2,3,4,5,6,7,8,9,10,11,12])
        

if __name__ == "__main__":
    unittest.main()