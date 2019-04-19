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

def testCheckPayRent(playermanagement, interface, board):
    player1 = Player("p1", 500, [], 1)
    playermanagement.playerBuy(player1, board)
    player2 = Player("p2", 500, [], 1)

    playermanagement.checkPayRent(player2, board)
    
    assert player2.money == 496, "Paying rent did not work"

if __name__ == "__main__":
    playerManagement = PlayerManager()
    interface = TextInterface()
    boardManager = BoardManager()
    board = boardManager.generateBoard()
    
    #testPlayerBuy(playerManagement, interface, board)

    testCheckPayRent(playerManagement, interface, board)