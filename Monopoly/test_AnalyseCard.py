"""
Unit Test for AnaliseCard.py
"""

import unittest
from AnalyseCard import AnaliseChance

class MyTest(unittest.TestCase):
    def test_AnaliseChance_Analise(self):
        self.assertEqual(AnaliseChance.Analise("You win £50"), 50)
        self.assertEqual(AnaliseChance.Analise("You lose £50"), -50)
        
    def test_AnaliseChance_doCardAction(self):

        class Player:
            def __init__(self):
                self.money = 0
        
        player = Player()

        self.assertEqual(AnaliseChance.doCardAction(player, "50").money, 50)
        self.assertEqual(AnaliseChance.doCardAction(player, "-50").money, 0)


if __name__ == "__main__":
    unittest.main()
