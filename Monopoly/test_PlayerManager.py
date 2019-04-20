"""
Unit Tests for PlayerManager.py
"""

import unittest
from PlayerManager import PlayerManager

class Interface:
    def getPlayerNames(self, numPlayers):
        return ["player1"]

class Property:
    def __init__(self, player):
        self.name = "property1"
        self.position = 1
        self.price = 500
        self.ownedBy = player
        self.rent = [500]
        self.numHouses = 0

class Player:
    def __init__(self, money, properties = None):
        self.money = money
        self.position = 1
        self.properties = [properties]

class MyTest(unittest.TestCase):

    def test_getPlayers(self):
        pm = PlayerManager()
        inter = Interface()

        self.assertIs(pm.getPlayers(1, inter)[0].name, "player1")
    
    def test_propertyPlayerOn(self):
        property1 = Property(Player(200))
        pm = PlayerManager()

        board = [property1]
        
        self.assertEqual(pm.propertyPlayerOn(1, board), property1)
    
    def test_playerBuy(self):
        player1 = Player(500)
        player2 = Player(0)
        pm = PlayerManager()
        property1 = Property(Player(200))

        board = [property1]

        self.assertEqual(pm.playerBuy(player1, board), True)
        self.assertEqual(pm.playerBuy(player2, board), False)
    
    def test_checkPayRent(self):
        player1 = Player(500)
        player2 = Player(0)

        property1 = Property(Player(200))
        property2 = Property(player2)

        pm = PlayerManager()

        board1 = [property1]
        board2 = [property2]

        self.assertEqual(pm.checkPayRent(player1, board1), True)
        self.assertEqual(pm.checkPayRent(player2, board2), False)
    

if __name__ == "__main__":
    unittest.main()