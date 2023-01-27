"""
Write a Python program to create a list whose ith element is the maximum of
the first i elements from a input list. Go to the editor
Input:
[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
Output:
[0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]
Input:
[6, 5, 4, 3, 2, 1]
Output:
[6, 6, 6, 6, 6, 6]
Input:
[1, 19, 5, 15, 5, 25, 5]
Output:
[1, 19, 19, 19, 19, 25, 25]
"""


def test(numbers):
    max_numbers = []
    for i in range(1, len(numbers) + 1):
        max_numbers.append(max(numbers[:i]))

    return max_numbers


numbers = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
print(test(numbers))

numbers = [6, 5, 4, 3, 2, 1]
print(test(numbers))
