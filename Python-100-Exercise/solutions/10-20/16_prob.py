"""16.
Write a Python program find the strings in a given list containing a given
substring. Go to the editor
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']
Input:
[(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
[]
"""


def test(s):
    prefix = s[0][0]
    return [s[0][1][w] for w in range(len(s[0][1])) if prefix in s[0][1][w]]


words = [("ca", ('cat', 'car', 'fear', 'center'))]
print(test(words))

words = [("o", ('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
print(test(words))

words = [("oe", ('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
print(test(words))
