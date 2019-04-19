"""
File that holds the BoardManager class.
"""

from Conversion import Conversions
import json

class BoardManager:
    def generateBoard(self):
        board = []
        with open('MonopolyData.json', 'r') as fp:
            listSquares = json.load(fp)
        for position in listSquares:
            board.append(Conversions.jsonToObj(position))
        return board

    def printBoard(self, board):
        for item in board:
            item.prettyPrint()
    
    def gameWon(self, players):
        bankruptPlayer = []
        for player in players:
            if player.money < 0:
                bankruptPlayer.append(player)
        if len(bankruptPlayer) >= len(players)-1:
            return True
        else:
            return False