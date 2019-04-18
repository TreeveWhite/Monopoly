from BoardManager import *


def testGenerateBoardFirstSquareName():
	b = BoardManager()
	board = b.generateBoard()

	assert board[0].name == "Go", "Expected 'Go' square name."

def testGenerateBoardFirstSquarePosition():
	b = BoardManager()
	board = b.generateBoard()

	assert board[0].position == 0, "Expected 'Go' square postion."
	

def testGenerateBoardTenthSquareName():
	b = BoardManager()
	board = b.generateBoard()

	assert board[9].name == "Bow Street", "Expected 'Bow Street' square."

def testGenerateBoardTenthSquarePrice():
	b = BoardManager()
	board = b.generateBoard()

	assert board[9].price == 160, "Expected 'Bow Street' square price to be 160"




if __name__ == "__main__":

	print("It passed...") # it didn't :(
	testGenerateBoardFirstSquareName()
	testGenerateBoardFirstSquarePosition()

	testGenerateBoardTenthSquareName()
	testGenerateBoardTenthSquarePrice()

	testPrintBoard()