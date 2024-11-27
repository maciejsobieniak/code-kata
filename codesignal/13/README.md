## Task description
You are provided with a string of alphanumeric characters in which each number, regardless of the number of digits, is always followed by at least one alphabetic character before the next number appears. The task requires you to return a transformed version of the string wherein the first alphabetic character following each number is moved to a new position within the string and characters in between are removed.

Specifically, for each number in the original string, identify the next letter that follows it, and then reposition that character to directly precede the number. All spaces and punctuation marks between the number and the letter are removed.

The length of the string s ranges from 3 to 106106 (inclusive), and the string contains at least one number. The numbers in the string are all integers and are non-negative.

Here is an example for better understanding:

Given the string:

"I have 2 apples and 5! oranges and 3 grapefruits."

The function should return:

"I have a2pples and o5ranges and g3rapefruits."

In this instance, the character 'a' following the number 2 is moved to come before the 2, the 'o' succeeding the 5 is placed before the 5, and the 'g' subsequent to the 3 is repositioned to precede the 3. Punctuation marks and spaces in between are removed.

Please note that the operation should maintain the sequential order of the numbers and the rest of the text. Considering this, the task is not solely about dividing a string into substrings but also about modifying them. This will test your expertise in Python string operations and type conversions.
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
