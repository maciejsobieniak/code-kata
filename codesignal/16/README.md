## Task description
You are given an initial date as a string in the format YYYY-MM-DD, along with an integer n which represents a number of days. Your task is to calculate the date after adding the given number of days to the initial date and return the result in the YYYY-MM-DD format.

Keep these points in mind when resolving the task:

    The initial date string is always valid, formatted as YYYY-MM-DD, where YYYY denotes the year, MM the month, and DD the day.
    The given integer n is the number of days you have to add to the initial date and will be up to 50,00050,000.
    The output should be a string showcasing the final date after adding n days, in the YYYY-MM-DD format.

Your function will be in the form add_days(date: str, n: int) -> str.

Constraints

    date = the date string in the YYYY-MM-DD format. The year YYYY will be from 1900 to 2100, inclusive. The month MM and the day DD will be valid for the given year.
    n = the integer representing the number of days you have to add to the initial date. n ranges from 1 to 50,00050,000, inclusive.
    You should consider leap years in the calculation. A year is a leap year if it is divisible by 4, but century years (years divisible by 100) are not leap years unless they are divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.
    The month and day result should always be two digits long, padding with a 0 if necessary. For example, July 9th should be formatted as "07-09".

Example

For date = '1999-01-01' and n = 365, the output should be '2000-01-01'.
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
