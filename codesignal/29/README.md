## Task description
For this task, you are given two non-negative integers, num1 and num2. However, these are not just ordinary numbers; they are so large that they should be represented as strings instead of normal integers. Each can be up to 100 digits long.

Your mission is to write a Python function that compares these two "string-numbers" without converting the entire strings into integers. Your function should determine whether num1 is greater than, less than, or equal to num2.

Your function can only use comparison operators (such as >, <, or ==) on strings. So “1” < “2” is allowed, but 1 < 2 is not. The task requires that you manually compare the two strings from the most significant digit to the least significant. You should implement your own logic to compare two string numbers.

The function should return the following results:

    If num1 is greater than num2, your function should return 1.
    If num2 is greater than num1, your function should return -1.
    If num1 and num2 are equal, your function should return 0.

Let's look at the following examples:

For `num1` = '12345' and `num2` = '1234', your function should return `1`.

For `num1` = '1234' and `num2` = '12345', your function should return `-1`.

For `num1` = '12345' and `num2` = '12345', your function should return `0`.

This exercise is a great test of your understanding of how numbers and strings work and interact in a programming language. We hope you find it challenging and enjoyable!

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
