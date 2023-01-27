"""
Write a Python program to sort the numbers of a given list by the sum of their
digits. Go to the editor
Input: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Output:
[10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]
Input: [23, 2, 9, 34, 8, 9, 10, 74]
Output:
[10, 2, 23, 34, 8, 9, 9, 74]
"""


def test(nums):
    return sorted(nums, key=lambda x: sum(int(i) for i in str(x)))


nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(test(nums))

nums = [23, 2, 9, 34, 8, 9, 10, 74]
print(test(nums))