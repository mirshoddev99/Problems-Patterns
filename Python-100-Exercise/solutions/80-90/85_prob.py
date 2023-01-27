"""Write a Python program to find an increasing sequence consisting of the
elements of the original list. Go to the editorInput:
[1, 3, 79, 10, 4, 2, 39]
Output:
[1, 2, 3, 4, 10, 39, 79]
Input:
[11, 31, 40, 68, 77, 93, 48, 1, 57]
Output:
[1, 11, 31, 40, 48, 57, 68, 77, 93]
Input:
[9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
Output:
[-3, -2, -1, 0, 2, 3, 4, 8, 9]"""


def test(n):
    return sorted(set(n))


nums = [1, 3, 79, 10, 4, 2, 39]
print(test(n=nums))

nums = [9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
print(test(n=nums))