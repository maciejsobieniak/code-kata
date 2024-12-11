## Task description
In this task, we are manipulating sentences and strings using nested loops. You will be given a string representing a sentence where words are separated by spaces. Your objective is to write a Python function that selects the even-indexed characters of words containing an odd number of characters.

This sentence string will have a maximum length of 500 characters, including spaces.

Subsequently, these characters must be combined into a single string in the order they appear in the sentence, but the final output string will be reversed end-to-end.

For instance, if the input sentence is "Coding tasks are fun and required", the output string should be "tssaefnad", which, when reversed, becomes "danfeasst". The words "tasks", "are", "fun", and "and" are selected since they have an odd number of characters, and the characters 't', 's', 's', 'a', 'e', 'f', 'n', 'a', 'd' at even indexes are chosen and then reversed in the final string. Do not forget that Python indexing begins at 0, so 't' in "tasks" is considered to be at an even index. Single-character words must also be taken into consideration for this task.
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
