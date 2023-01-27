"""
Write a Python program to find the product of the units digits in the numbers
of a given list. Go to the editor
Input:
[12,23]
Output:
6
Input:
[12, 23, 43]
Output:
18
Input:
[113, 234]
Output:
12
Input:
[1002, 2005]
Output:
10
"""


def test(n):
    product_n = 1
    for i in n:
        product_n *= int(str(i)[-1])
    return product_n


n = [1002, 2005]
print(test(n))

n = [12, 23, 43]
print(test(n))
