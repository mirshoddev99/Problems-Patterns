"""
Write a Python program to compute the product of the odd digits in a given
number, or 0 if there aren't any. Go to the editor
Input: 123456789
Output:
945
Input: 2468
Output:
0
Input: 13579
Output:
945
"""


def test(n):
    if not any(int(c) % 2 != 0 for c in str(n)):
        return 0
    else:
        p = 1
        for i in str(n):
            if int(i) % 2 != 0:
                p *= int(i)
    return p


num = 123456789
print(test(num))

num = 2468
print(test(num))

num = 13579
print(test(num))
