"""
Unit Tests for PlayerManager
"""

from PlayerManager import *
from TextInterface import *

def testPlayerBuy(playermanagement, interface):
    player = Player("p1", 500, [], 1)
    playermanagement.playerBuy(player, board)

    assert player.properties[0].name == "Mediterranean Avenue", "Buying does not work"

if __name__ == "__main__":
    playermanagement = PlayerManager()
    interface = TextInterface()
    testPlayerBuy(playermanagement, interface)