"""
Unit Tests for Player.py
"""

import unittest
from Player import Player

class MyTest(unittest.TestCase):
    def test_movePlayer(self):
        board = ["", "", "", "", "", "", "", "", "", "", "", ""]
        player1 = Player("player1", 1000, [], 0)

        player1.movePlayer(9, board)
        self.assertEqual(player1.position, 9)
    
    def test_playerPassGo(self):
        player1 = Player("player1", 0, [], 0)

        player1.playerPassGo()
        self.assertEqual(player1.money, 200)

if __name__ == "__main__":
    unittest.main()
