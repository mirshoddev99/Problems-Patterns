"""
Write a Python program to find the sum of the even elements that are at odd
indices in a given list. Go to the editor
Input:
[1, 2, 3, 4, 5, 6, 7]
Output:
12
Input:
[1, 2, 8, 3, 9, 4]
Output:
6
"""


def test(nums):
    result = sum([i for i in nums[1::2] if i % 2 == 0])
    return result


numbers = [1, 2, 8, 3, 9, 4]
print(test(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7]
print(test(numbers))
