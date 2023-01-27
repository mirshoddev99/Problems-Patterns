"""
Write a Python program to shift the decimal digits n places to the left,
wrapping the extra digits around. If shift > the number of digits of n, reverse the
string. Go to the editor
Input:
n = 12345 and shift = 1
Output:
Result = 23451
Input:
n = 12345 and shift = 2
Output:
Result = 34512
Input:
n = 12345 and shift = 3
Output:
Result = 45123
Input:
n = 12345 and shift = 5
Output:
Result = 12345
Input:
n = 12345 and shift = 6
Output:
Result = 54321
"""

from collections import deque


def test(n, shift):
    if shift > len(n):
        return n[::-1]
    else:
        my_deq = deque([i for i in " ".join(n).split()])
        my_deq.rotate(-shift)
        return "".join(my_deq)


num_str = "12345"
shift = 1
print(test(num_str, shift))

num_str = "12345"
shift = 5
print(test(num_str, shift))

num_str = "12345"
shift = 6
print(test(num_str, shift))