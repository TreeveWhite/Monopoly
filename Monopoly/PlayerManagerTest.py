"""
Unit Tests for PlayerManager
"""

from PlayerManager import *
from TextInterface import *

def testPlayerBuy(playermanagement, interface):
    player = Player("p1", 500, [], 1)
    playermanagement.playerBuy(player, board)

    assert player.properties[0].name == "Mediterranean Avenue", "Buying does not work"

def testGetPlayers(playermanagement, interface):
    numPlayers = 2
    print(playermanagement.getPlayers(numPlayers, interface))

def testProotertyPlayeron(playermanagement, interface):
    #Unit test the func propteryp player on ie make a player object and pass into fuc check it gives right pos.

if __name__ == "__main__":
    playermanagement = PlayerManager()
    interface = TextInterface()
    testPlayerBuy(playermanagement, interface)