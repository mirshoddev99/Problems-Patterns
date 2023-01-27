"""
19. Write a Python program to split a given string (s) into strings if there is a
space in the string, otherwise split on commas if there is a comma, otherwise
return the list of lowercase letters with odd order (order of a = 0, b = 1, etc.) Go to
the editor
Input:
a b c d
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['a', 'b', 'c', 'd']
Input:
a,b,c,d
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['a', 'b', 'c', 'd']
Input:
abcd
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['b', 'd']
"""

import re


def test(w):
    ls = []

    if re.search(r"(\s|,)", w):
        for s in range(0, len(w), 2):
            ls.append(w[s])

    return ls

strings = "a,b,c,d"
print(test(strings))

strings = "a b c d"
print(test(strings))














