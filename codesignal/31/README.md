## Task description
You are tasked with writing a Python function to multiply two extremely large positive integers. These are not your regular-sized large numbers; they are represented as strings potentially up to 500 digits long.

Your function should take two string parameters, representing the two large integers to be multiplied, and return the product as a string. The challenging part is that you should perform the multiplication without converting the entire strings into integers.

Keep in mind that the elements of the string are digits in the range from 0 to 9, inclusive.

Furthermore, bear in mind that when multiplying numbers manually, we align the numbers vertically and multiply each digit of the first number with each digit of the second number, starting from the rightmost digits, and add the results after shifting appropriately.

Please solve this problem using similar, decision-based string manipulations instead of merely converting strings into integers, multiplying them, and converting the result back to a string. This approach is imperative as direct multiplication would not be feasible for very large numbers.
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
