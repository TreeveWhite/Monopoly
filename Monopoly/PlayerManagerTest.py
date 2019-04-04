"""
Unit Tests for PlayerManager
"""

from PlayerManager import *
from TextInterface import *
from BoardManager import *

def testPlayerBuy(playermanagement, interface, board):
    player = Player("p1", 500, [], 1)
    didByWork = playermanagement.playerBuy(player, board)

    assert player.properties[0].name == "Mediterranean Avenue", "Buying does not work"
    assert didByWork == True, "Buying - was expecting true, got false"

if __name__ == "__main__":
    playerManagement = PlayerManager()
    interface = TextInterface()
    boardManager = BoardManager()
    board = boardManager.generateBoard()
    
    testPlayerBuy(playerManagement, interface, board)