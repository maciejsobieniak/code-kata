import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from solution import stringSearch

class TestStringSearch(unittest.TestCase):
    def test_case_1(self):
        sourceArray = [(1, 'abc'), (2, 'def'), (3, 'xyz')]
        searchArray = [(1, 'abcdef'), (5, 'uvwxy')]
        expected_output = [(1, 'abc')]
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_2(self):
        sourceArray = [(1, 'abc')]
        searchArray = [(2, 'def')]
        expected_output = []
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_3(self):
        sourceArray = [(1, 'abc'), (2, 'def')]
        searchArray = [(3, 'abc'), (4, 'def')]
        expected_output = [(1, 'abc'), (2, 'def')]
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_4(self):
        sourceArray = [(1, 'abc'), (2, 'def'), (3, 'ghi'), (4, 'jkl')]
        searchArray = [(5, 'mnopqr')]
        expected_output = []
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_5(self):
        sourceArray = [(1, 'abc'), (2, 'def'), (3, 'ghi')]
        searchArray = [(4, 'abcdefghi'), (5, 'defghiabc')]
        expected_output = [(1, 'abc'), (2, 'def'), (3, 'ghi')]
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_6(self):
        sourceArray = [(1, 'var'), (2, 'ans'), (3, 'tes')]
        searchArray = [(4, 'variant'), (5, 'answertest'), (6, 'tesla')]
        expected_output = [(1, 'var'), (2, 'ans'), (3, 'tes')]
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_7(self):
        sourceArray = [(1, 'ab'), (2, 'bc'), (3, 'cd')]
        searchArray = [(4, 'abcd'), (5, 'bcda')]
        expected_output = [(1, 'ab'), (2, 'bc'), (3, 'cd')]
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)


if __name__ == '__main__':
    unittest.main()