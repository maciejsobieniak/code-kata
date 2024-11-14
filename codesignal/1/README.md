## Task description
Provided with a string of n lowercase English alphabet letters (from 'a' to 'z'), where n ranges from 1 to 100, inclusive. You must create a new string by selecting characters from the given string in a specific order: select each character that comes k characters after the previous selection in the string. If you reach the end of the string, you should continue from the beginning.

Write a Python function, repeat_char_jump(inputString, step). The function takes two parameters: inputString and step, where inputString is the string you are working with, and step is an integer that denotes the number of characters to skip with each jump. The value of step ranges from 1 to the length of the input string. The function should return a newly formed string consisting of characters selected in the order dictated by the jump length step.

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
