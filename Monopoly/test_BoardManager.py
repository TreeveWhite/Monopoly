"""
Unit Test for BoardManager.py
"""

from BoardManager import BoardManager
import unittest

class MyTest(unittest.TestCase):

	def test_GenerateBoardFirstSquareName(self):
		b = BoardManager()
		board = b.generateBoard()

		assert board[0].name == "Go", "Expected 'Go' square name."

	def test_GenerateBoardFirstSquarePosition(self):
		b = BoardManager()
		board = b.generateBoard()

		assert board[0].position == 0, "Expected 'Go' square postion."
		

	def test_GenerateBoardTenthSquareName(self):
		b = BoardManager()
		board = b.generateBoard()

		assert board[1].name == "Africa Avenue", "Expected 'Africa Avenue' square."

	def test_GenerateBoardTenthSquarePrice(self):
		b = BoardManager()
		board = b.generateBoard()

		assert board[1].price == 60, "Expected 'Africa Avenue' square price to be 60"




if __name__ == "__main__":
	unittest.main()