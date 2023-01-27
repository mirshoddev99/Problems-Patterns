"""
15. Write a Python program find the longest string of a given list of strings. Go to
the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter
"""


def test(s):
    return max(s, key=len)


string_list = ['cat', 'car', 'fear', 'center']
print(test(string_list))

string_list = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print(test(string_list))
