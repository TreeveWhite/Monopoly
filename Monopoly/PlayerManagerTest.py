"""
Unit Tests for PlayerManager
"""

from PlayerManager import *

def testPlayerBuy(playermanagement, interface):
    numPlayers = 2
    player = Player("p1", 500, [], 1)
    playermanagement.playerBuy(player)

    assert player.properties[0].name == "Mediterranean Avenue", "Buying does not work"

if __name__ == "__main__":
