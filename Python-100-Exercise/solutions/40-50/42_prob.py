"""
Write a Python program to find the set of distinct characters in a given string,
ignoring case. Go to the editor
Input: HELLO
Output:
['h', 'o', 'l', 'e']
Input: HelLo
Output:
['h', 'o', 'l', 'e']
Input: Ignoring case
Output:
['s', 'n', 'c', 'o', 'e', 'i', 'r', 'g', 'a', ' ']
"""


def test(strs):
    l = map(lambda w: w.lower(), strs)
    return list(set(l))


my_string = "HELLO"
print(test(my_string))

my_string = "Ignoring case"
print(test(my_string))

my_string = "HelLo"
print(test(my_string))
