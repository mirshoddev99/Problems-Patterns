"""
7. Write a Python program to check a given list of integers where the sum of the
first i integers is i. Go to the editor
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False
"""


def check_summ(n):

    return len(n) == sum(n)

print(check_summ([0, 1, 2, 3, 4, 5]))
print(check_summ([1, 1, 1, 1, 1, 1]))
print(check_summ([2, 2, 2, 2, 2]))