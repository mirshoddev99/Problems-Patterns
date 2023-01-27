"""
Write a Python program to find the h-index, the largest positive number h
such that h occurs in the sequence at least h times. If there is no such positive
number return h = -1. Go to the editor
Input:
[1, 2, 2, 3, 3, 4, 4, 4, 4]
Output:
4
Input:
[1, 2, 2, 3, 4, 5, 6]
Output:
2
Input:
[3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]
Output:
5
"""


def test(nums):
    if all(nums):
        return max(n for n in nums if nums.count(n) >= n)
    else:
        return -1


nums = [1, 2, 2, 3, 3, 4, 4, 4, 4]
print(test(nums))

nums = [0, -1]
print(test(nums))

nums = [1, 2, 2, 3, 4, 5, 6]
print(test(nums))

nums = [3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]
print(test(nums))