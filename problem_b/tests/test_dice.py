import unittest
from dice import Dice


class CalculateProbabilityTest(unittest.TestCase):
    """
    Test if app can succesfully calculate probability of dice rolls
    """

    def setUp(self):
        self._dice = Dice()

    def test1Sided(self):
        probability = 1.0
        self.assertEqual(probability, self._dice.roll(1))

    def test2Sided(self):
        probability = 0.5
        self.assertEqual(probability, self._dice.roll(2))

    def test3Sided(self):
        probability = 1.0 / 3.0
        self.assertEqual(probability, self._dice.roll(3))

    def test4Sided(self):
        probability = 0.25
        self.assertEqual(probability, self._dice.roll(4))

if __name__ == "__main__":
    unittest.main()
