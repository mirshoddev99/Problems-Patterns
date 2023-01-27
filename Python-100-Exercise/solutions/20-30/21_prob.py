"""21. Write a Python program to check, for each string in a given list, whether the
last character is an isolated letter or not. Return True or False. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]
Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True]"""

import re


def test(w):

    return ["True" if re.search(" ", word) else "False" for word in w]

words = ['cat', 'car', 'fear', 'center']
print(test(words))

words = ['ca t', 'car', 'fea r', 'cente r']
print(test(words))
