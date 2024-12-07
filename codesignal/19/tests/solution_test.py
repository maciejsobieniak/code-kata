import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from solution import spot_swaps

class SpotSwapsTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(spot_swaps("hello", "hlelo"), [(1, 'e', 'l')])

    def test2(self):
        self.assertEqual(spot_swaps("abcdef", "abcfed"), [])

    def test3(self):
        self.assertEqual(spot_swaps("goodbye", "godobye"), [(2, 'o', 'd')])

    def test4(self):
        self.assertEqual(spot_swaps("firsttest", "firtestst"), [])

    def test5(self):
        self.assertEqual(spot_swaps("pythonista", "pyhtonista"), [(2, 't', 'h')])

    def test6(self):
        self.assertEqual(spot_swaps("qwertyuiop", "qewrtyuiop"), [(1, 'w', 'e')])

    def test7(self):
        self.assertEqual(spot_swaps("hellothereworld", "helotlehreworld"), [(6, 'h', 'e')])

if __name__ == "__main__":
    unittest.main()