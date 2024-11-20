## Task description
Your task is to write a Python function that takes in a string and identifies all the consecutive groups of identical characters within it, with the analysis starting from the end of the string rather than from its beginning. A group is defined as a segment of the text where the same character is repeated consecutively.

Your function should return a list of tuples. Each tuple will consist of the repeating character and the number of its repetitions. For instance, if the input string is "aaabbcccdde", the function should output: [('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 3)].

Note that the input string cannot be empty; in other words, it must contain at least one character, and its length must not exceed 500 characters. The return should also be in reverse order, starting from the group of repeated characters at the end of the string and moving backward.

## Solution
My solution is in the solution.py file.

## Tests
Tests for the code-kat are in the tests directory.

## Technologies
python <= 3.10.6

## Contact
maciej@maciejsobieniak.pl

## This code-kata is from:
* [codesignal.com](https://codesignal.com) 
