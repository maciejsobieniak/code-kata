## Task description
You are given two lists of integers (listA and listB), each containing n elements, with n ranging from 1 to 50. Each element in both lists can range from -1000 to 1000, inclusive.

Your task is to write a Python function that identifies pairs of integers {a, b} wherein a belongs to listA and b belongs to listB, and a is greater than b. The function should return all such pairs in the order in which a appears in listA.

For instance, if listA consists of [5, 1, 8, -2, 0] and listB comprises [3, 2, 7, 10, -1], the output should be [(5, 3), (5, 2), (5, -1), (1, -1), (8, 3), (8, 2), (8, 7), (8, -1), (0, -1)].

Importantly, the order of elements in the output tuples should reflect the sequence in which a appears in listA. A pair cannot be included more than once. If no pair meets the condition, the function should return an empty list.

Hint: Solving this task requires the use of nested loops. The outer loop should iterate through listA and the inner loop through listB, checking the condition a > b during each iteration.
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
