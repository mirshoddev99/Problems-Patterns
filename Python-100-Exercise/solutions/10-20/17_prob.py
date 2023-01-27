"""
Write a Python program to create string consisting of the non-negative
integers up to n inclusive. Go to the editor
Input:
4
Output:
0 1 2 3 4
Input:
15
Output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
"""


def test(n):
    return ' '.join(map(str, range(n + 1)))


n = 4
print(test(n))

n = 15
print(test(n))
