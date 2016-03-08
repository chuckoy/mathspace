import unittest
from dice import roll
from decimal import *


class CalculateProbabilityTest(unittest.TestCase):
    """
    Test if app can succesfully calculate probability of dice rolls
    """

    def test1Sided(self):
        probability = Decimal(1)
        self.assertEqual(probability, roll(1))

    def test2Sided(self):
        probability = Decimal(1) / Decimal(2)
        self.assertEqual(probability, roll(2))

    def test3Sided(self):
        probability = Decimal(2) / Decimal(9)
        self.assertEqual(probability, roll(3))

    def test4Sided(self):
        probability = Decimal(6) / (Decimal(4) ** 3)
        self.assertEqual(probability, roll(4))

    def test5Sided(self):
        probability = Decimal(24) / (Decimal(5) ** 4)
        self.assertEqual(probability, roll(5))

if __name__ == "__main__":
    unittest.main()
