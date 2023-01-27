"""
Write a Python program to find which characters of a hexadecimal number
correspond to prime numbers. Go to the editor
Input: 123ABCD
Output:
[False, True, True, False, True, False, True]
Input: 123456
Output:
[False, True, True, False, True, False]
Input: FACE
Output:
[False, False, False, False]
"""


def test(strs):
    return ["True" if c in "2357BD" else "False" for c in strs]


my_hex = "123ABCD"
print(test(my_hex))
