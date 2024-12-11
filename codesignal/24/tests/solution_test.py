import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from solution import solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("Coding tasks are fun and required"), "danfeasst")

    def test2(self):
        self.assertEqual(solution("etrnal"), "")

    def test3(self):
        self.assertEqual(solution("awe-inspiring"), "giisiea")

    def test4(self):
        self.assertEqual(solution("a a"), "aa")

    def test5(self):
        self.assertEqual(solution("python coding"), "")

    def test6(self):
        self.assertEqual(solution("Hello, world!"), "")

    def test7(self):
        self.assertEqual(solution("Mastering Advanced Looping and Implementation"), "dagioLgiesM")

    def test8(self):
        self.assertEqual(solution("Stay hungry, Stay foolish."), ",rnh")

    def test9(self):
        self.assertEqual(solution("! o G e h C o s i M P"), "PMisoCheGo!")

    def test10(self):
        self.assertEqual(solution("abcdefghijklmnopqrstuvwxyz"), "")

if __name__ == '__main__':
    unittest.main()