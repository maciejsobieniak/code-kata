## Task description
In this task, You are provided with an array of n integers, where n can range from 1 to 200, inclusive. Your task is to create a new array that takes two pairs of 'opposite' elements from the original array at each iteration, starting from the center and moving towards both ends, to calculate the resulting multiplication of each pair.

By 'opposite' elements, we mean pairs of elements symmetrically located relative to the array's center. If the array's length is odd, the center element doesn't have an opposite and should be included in the result array as is.

Each element in the array can range from -100 to 100, inclusive.

For example, if the input array is [1, 2, 3, 4, 5], the returned array should be [3, 8, 5]. This is because the center element 3 remains as it is, the multiplication of 2 and 4 is 8, and the multiplication of 1 and 5 is 5.

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
