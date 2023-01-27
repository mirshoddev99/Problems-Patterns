""" Write a Python program to find the sublist of numbers from a given list of
numbers with only odd digits in increasing order. Go to the editor
Input:
[1, 3, 79, 10, 4, 2, 39]
Output:
[1, 3, 39, 79]
Input:
[11, 31, 40, 68, 77, 93, 48, 1, 57]
Output:
[1, 11, 31, 57, 77, 93]
Input:
[9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
Output:
[-3, -1, 3, 9]"""


def test(nums):
    result = list(filter(lambda x: x % 2 != 0, nums))
    return sorted(result)


numbers = [1, 3, 79, 10, 4, 2, 39]
print(test(numbers))

numbers = [9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
print(test(numbers))