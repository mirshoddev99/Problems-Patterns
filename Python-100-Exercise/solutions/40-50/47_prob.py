""" Write a Python program to Filter for the numbers in numbers in a given list
whose sum of digits is > 0, where the first digit can be negative. Go to the editorInput:
[11, -6, -103, -200]
Output:
[11, -103]
Input:
[1, 7, -4, 4, -9, 2]
Output:
[1, 7, 4, 2]
Input:
[10, -11, -71, -13, 14, -32]
Output:
[10, -13, 14]"""


def test(nums):
    return [n for n in nums if int(str(n)[:2]) + sum(map(int, str(n)[2:])) > 0]


n = [11, -6, -103, -200]
print(test(n))
