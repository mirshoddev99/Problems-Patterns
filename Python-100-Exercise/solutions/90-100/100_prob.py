"""Write a Python program to find four positive even integers whose sum is a
given integer. Go to the editor
Input:
n = 100
Output:
[94, 2, 2, 2]
Input:
n = 1000
Output:
[994, 2, 2, 2]
"""


def test(n):
    from random import sample
    nums = list(range(0, n + 1, 2))
    while True:
        check_nums = sample(nums, 4)
        if sum(check_nums) == n:
            return check_nums


n = 100
print(test(n))
