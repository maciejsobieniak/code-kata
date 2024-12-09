## Task description
You are given two lists: sourceArray and searchArray, consisting of n and m tuples respectively, where n is an integer such that 1 ≤ n ≤ 100 and m is an integer such that 1 ≤ m ≤ 500. Each tuple in both arrays contains two elements: an integer identifier and a string. The identifiers in both arrays range from 1 to 100, inclusive. The strings in sourceArray consist of alphanumeric characters with lengths ranging from 1 to 100, inclusive. The strings in searchArray have lengths ranging from 1 to 500, inclusive.

Your task is to implement a function stringSearch(sourceArray, searchArray) that takes these two arrays as input and returns an array that includes all tuples from sourceArray for which its string is a substring of at least one string in any tuple from searchArray and the identifier of the source tuple is less than or equal to the identifier of the search tuple.

The order in which the tuples appear in the result should reflect their original order in the sourceArray. If no matches are found, the function should return an empty array.

For example, if sourceArray = [(1, 'abc'), (2, 'def'), (3, 'xyz')] and searchArray = [(1, 'abcdef'), (5, 'uvwxy')], the function should return [(1, 'abc')] since 'abc' and 'def' are substrings found in 'abcdef', but 'def' is associated with 2 in sourceArray which is not less than or equal to 1 in searchArray. The string 'xyz' is not found in either 'abcdef' or 'uvwxy', so it is not included in the result.

This task requires mastery of skills in nested looping and array manipulation, especially in the context of searching for a string within other strings.
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
