import unittest
from AnalyseCard import AnaliseChance

class MyTest(unittest.TestCase):
    def test_AnaliseChance_Analise(self):

        class Player:
            def __init__(self):
                self.money = 0
        
        player = Player()

        self.assertEqual(AnaliseChance.Analise("You win £50", player), 50)
        self.assertEqual(AnaliseChance.Analise("You lose £50", player), 0)


if __name__ == "__main__":
    unittest.main()
