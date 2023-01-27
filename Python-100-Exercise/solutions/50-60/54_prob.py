"""Write a Python program to remove duplicates from a list of integers,
preserving order. Go to the editor
Input:
[1, 3, 4, 10, 4, 1, 43]
Output:
[1, 3, 4, 10, 43]
Input:
[10, 11, 13, 23, 11, 25, 23, 76, 99]
Output:
[10, 11, 13, 23, 25, 76, 99]"""


def test(n):
    return sorted(set(n))


nums = [1, 3, 4, 10, 4, 1, 43]
print(test(nums))

nums = [10, 11, 13, 23, 11, 25, 23, 76, 99]
print(test(nums))