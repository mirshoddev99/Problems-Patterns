"""Given an array of numbers representing a branch on a binary tree, write a
Python program to find the minimum even value and its index. In the case of a
tie, return the smallest index. If there are no even numbers, the answer is []. Go
to the editor
Input:
[1, 9, 4, 6, 10, 11, 14, 8]
Output:
Minimum even value and its index of the said array of numbers:
[4, 2]
Input:
[1, 7, 4, 4, 9, 2]
Output:
Minimum even value and its index of the said array of numbers:
[2, 5]
Input:
[1, 7, 7, 5, 9]
Output:
Minimum even value and its index of the said array of numbers:
[]"""


def test(binary_tree):
    get_min = 0
    if any(c % 2 == 0 for c in binary_tree):
        get_min = min(i for i in tree if i % 2 == 0)
    else:
        return []
    return [get_min, binary_tree.index(get_min)]


tree = [1, 9, 4, 6, 10, 11, 14, 8]
print(test(tree))

tree = [1, 7, 4, 4, 9, 2]
print(test(tree))

tree = [1, 7, 7, 5, 9]
print(test(tree))