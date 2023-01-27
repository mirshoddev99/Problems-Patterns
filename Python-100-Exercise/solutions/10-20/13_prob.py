"""
Write a Python program to find the strings in a given list, starting with a given
prefix. Go to the editor
Input:
[( ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']Input:
[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
Output:
['dog', 'donut']
"""


def test(words):
    prefix = words[0][0]
    ls = [words[0][1][w] for w in range(len(words[0][1])) if words[0][1][w].startswith(prefix)]

    return ls


words = [("ca", ('cat', 'car', 'fear', 'center'))]
print(test(words))

words = [("do", ('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
print(test(words))
