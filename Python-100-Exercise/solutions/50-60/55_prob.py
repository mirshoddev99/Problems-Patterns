"""Write a Python program to find the numbers that are greater than 10 and
have odd first and last digits. Go to the editor
Input:
[1, 3, 79, 10, 4, 1, 39, 62]
Output:
[79, 39]
Input:
[11, 31, 77, 93, 48, 1, 57]
Output:
[11, 31, 77, 93, 57]"""


def test(n):
    return [i for i in n if i > 10 and int(str(i)[0]) % 2 != 0 and int(str(i)[-1]) % 2 != 0]


nums = [1, 3, 79, 10, 4, 1, 39, 62]
print(test(nums))

nums = [11, 31, 77, 93, 48, 1, 57]
print(test(nums))