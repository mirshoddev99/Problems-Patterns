"""
Write a Python program to find the largest number where commas or periods
are decimal points. Go to the editor
Input:
['100', '102,1', '101.1']
Output:
102.1
"""


def test(str_numbers):
    return max(float(n.replace(",", ".")) for n in str_numbers)


numbers = ['100', '102,1', '101.1']
print(test(numbers))

numbers = ['100', '102,1', '103.1']
print(test(numbers))
