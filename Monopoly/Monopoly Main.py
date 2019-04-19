"""
Program that creates a Monopoly game
"""

from BoardManager import *
from Conversion import *
from Dice import *
from Player import *
from PlayerManager import *
from SquareClasses import *
from TextInterface import *

if __name__ == "__main__":
    #Initialise any classes as objects so easy to rename/reasign
    boardManager = BoardManager()
    currentInterface = TextInterface()
    playerManager = PlayerManager()

    #Initialise the game
    currentInterface.showWelcome()
    board = boardManager.generateBoard()
    numberPlayers = currentInterface.getNumPlayers()
    players = playerManager.getPlayers(numberPlayers, currentInterface)

    #Play game
    while boardManager.gameWon != True:
        for player in players:
            playerManager.takeTurn(player, board, currentInterface)
            currentInterface.showDetails(player, board)
        