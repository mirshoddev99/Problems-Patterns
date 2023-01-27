"""
Write a Python program to determine the direction ('increasing' or
'decreasing') of monotonic sequence numbers. Go to the editor
Input:
[1, 2, 3, 4, 5, 6]
Output:
Increasing.
Input:
[6, 5, 4, 3, 2, 1]
Output:
Decreasing.
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
Not a monotonic sequence!
"""


def test(n):
    return "Increasing." if all(n[i] < n[i + 1] for i in range(len(n) - 1)) else \
        "Decreasing." if all(n[i] > n[i + 1] for i in range(len(n) - 1)) else \
            "Not a monotonic sequence!"


numbers = [1, 2, 3, 4, 5, 6]
print(test(numbers))

numbers = [6, 5, 4, 3, 2, 1]
print(test(numbers))

numbers = [19, 19, 5, 5, 5, 5, 5]
print(test(numbers))
