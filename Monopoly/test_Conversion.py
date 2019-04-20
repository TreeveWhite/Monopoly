"""
Unit Tests for Conversion.py
"""

import unittest
from Conversion import Conversions

class MyTest(unittest.TestCase):
    def test_JsonToObj(self):
        dictionary = {'__class__': 'GoSquare', '__module__': 'SquareClasses', 'name': 'Go', 'position': 0}

        self.assertEqual(Conversions.jsonToObj(dictionary).name, "Go")
        
if __name__ == "__main__":
    unittest.main()