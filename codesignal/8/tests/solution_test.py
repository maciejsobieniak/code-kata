import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("aaababbababaca"), "aa1ab2ba3ca1")

    def test2(self):
        self.assertEqual(solution("abcabcabcabcab"), "ab1ca1bc1ab1ca1bc1ab1")

    def test3(self):
        self.assertEqual(solution("ab"), "ab1")

    def test4(self):
        self.assertEqual(solution("ccddaaeeff"), "cc1dd1aa1ee1ff1")

    def test5(self):
        self.assertEqual(solution("eeffgg"), "ee1ff1gg1")

if __name__ == '__main__':
    unittest.main()