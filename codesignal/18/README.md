## Task description
You are given two lists, sentences and words, each comprising n strings, where n ranges from 11 to 100100 inclusive. Each string in the sentences list has a length ranging from 11 to 500500 inclusive. Each word in the words list is a single lowercase English alphabet word of length 11 to 1010 inclusive.

Your task is to find all instances of each word in the corresponding sentence from the sentences list and replace them with the reverse of the word. The words and sentences at the same index in their respective lists are deemed to correspond to each other.

Return a new list comprising n strings, where each string is the sentence from the sentences list at the corresponding index, with all instances of the word from the words list at the same index replaced with its reverse.

If the word is not found in the respective sentence, keep the sentence as it is.

Remember, while replacing the instances of word in the sentence, you should preserve the case of the initial letter of the word. If a word starts with a capital letter in the sentence, its reversed form should also start with a capital letter.

Example

For sentences = ['this is a simple example.', 'the name is bond. james bond.', 'remove every single e'] and words = ['simple', 'bond', 'e'], the output should be ['this is a elpmis example.', 'the name is dnob. james dnob.', 'remove every single e'].
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
