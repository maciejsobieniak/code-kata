## Task description
You are the developer of a unique board game and are now dealing with the challenge of quantifying player progress, assuming different starting positions.

The game is played on a linear board that can be described as an array of integers, from 1 to n, with n ranging from 11 to 500500 inclusive. Each position in the array is a move value that a player can take, signifying the number of steps a player can move rightward. An obstacle is a specific integer value on which the player cannot land.

Your task is to implement the solution(numbers, obstacle) function, which calculates and returns an array steps. For every i in steps, the algorithm should calculate the number of steps required for a player to reach the end of the array from the i-th position without landing on an obstacle. If the player encounters an obstacle, steps[i] should should be -1.

Each number in the numbers array can range from 11 to 1010, and the obstacle value can range between 11 and 1010, inclusive.

The return value should be steps, the array with calculated values.

For example, if numbers is [5, 3, 2, 6, 2, 1, 7] and obstacle is 3, the function would return an array [3, -1, 3, 1, 2, 2, 1]. The first value 1 indicates that starting from position 0, the player will have to make one move and land on an obstacle. The second value, -1, indicates that starting from 1, the player is on an obstacle. Therefore, progression from 1 is not possible. And so on.

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
