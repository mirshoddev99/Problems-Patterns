"""
Write a Python program to find the number which when appended to the list
makes the total 0. Go to the editor
Input:
[1, 2, 3, 4, 5]
Output:
-15
Input:
[-1, -2, -3, -4, 5]
Output:
5
Input:
[10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]
Output:
-1316384
"""


def test(nums):
    n = -sum(nums) if sum(nums) else sum(nums)
    return n


numbers = [1, 2, 3, 4, 5]
print(test(numbers))

numbers = [-1, -2, -3, -4, 5]
print(test(numbers))

numbers = [10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]
print(test(numbers))