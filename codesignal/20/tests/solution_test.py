import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from solution import common_elements

class CommonElementsTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(common_elements([7, 2, 3, 9, 1], [2, 3, 7, 6]), [7, 2, 3])

    def test2(self):
        self.assertEqual(common_elements([1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]), [])

    def test3(self):
        self.assertEqual(common_elements([1, 2, 3], [2, 3, 4, 1]), [1, 2, 3])

    def test4(self):
        self.assertEqual(common_elements([1, 2, 3], [3, 2, 1, 4, 5, 6]), [1, 2, 3])

    def test5(self):
        self.assertEqual(common_elements([1, 2, 3], []), [])

    def test6(self):
        self.assertEqual(common_elements([-1, -2, -3, -4, -5], [-2, -4]), [-2, -4])

    def test7(self):
        self.assertEqual(common_elements([1, 2, 3], [1, 3]), [1, 3])


if __name__ == "__main__":
    unittest.main()