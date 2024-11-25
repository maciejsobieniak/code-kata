## Task description
you are given a string that contains a series of words separated by a hyphen ("-"). Each word in the string can be a lowercase letter from 'a' to 'z' or a set of digits representing a number from 1 to 26. Your task is to parse this string and swap the type of each word: convert numbers into their corresponding English alphabet letters, and letters into their numerical equivalents. This means '1' should convert to 'a', and 'a' should convert to '1'.

You need to return a new string with the converted words, rejoined with hyphens.

Ensure you maintain the original order of the words from the input string in your output string.

The input string's length should range from 1 to 1000 for this exercise. The string will never be empty, always containing at least one valid lowercase letter or numerical word.

Remember, the transformation of words should be limited to converting numbers from 1 to 26 into their corresponding letters from 'a' to 'z', and vice versa.

Example

For the input string "1-a-3-c-5", the output should be "a-1-c-3-e".
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
