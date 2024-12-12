## Task description
You are given a string that represents a sentence in which words are separated by spaces. Your task is to create a Python function that identifies and concatenates the second half of each word with an even number of characters, ensuring the characters of this second half go before the character c in the ASCII table. Then, combine these characters into a single string, maintaining the order in which they appear in the sentence.

The input sentence consists of ASCII characters from the space character (' ') up to the tilde character ('~'), with its length ranging between 1 and 500, inclusive. These characters form words separated by spaces, without any consecutive space characters.

For example, consider the sentence: "Python is a high-level programming language." and the character "n". The word 'Python' consists of 6 characters (an even number), and the second half of this word is 'hon'. In this second half, only 'h' is less than 'n'.

The output of your function, in this case, should be: "h", as it's the only character that meets the conditions.

For the character comparison ('<' character), use the ASCII values since all characters in the sentence are ASCII. ASCII codes for characters can be found by using Python's built-in function ord().

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
