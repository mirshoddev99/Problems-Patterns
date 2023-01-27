"""
Write a Python program to determine which triples sum to zero from a given
list of lists. Go to the editor
Input: [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
Output:
[False, True, True, False, True]
Input: [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]
Output:[True, True, False, False, False]
"""


def test(n):
    return [True if sum(i) == 0 else False for i in n]


nums = [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
print(test(nums))

nums = [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]
print(test(nums))