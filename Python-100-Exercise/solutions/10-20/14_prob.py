"""
14. Write a Python program to find the lengths of a given list of non-empty
strings. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]
"""

def test(s):

    return [len(word) for word in s]

strings = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print(test(strings))

