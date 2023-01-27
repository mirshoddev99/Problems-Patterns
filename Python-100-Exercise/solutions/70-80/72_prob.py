"""Write a Python program to find the indices of three numbers that sum to 0 in
a given list of numbers. Go to the editor
Input: [12, -7, 3, -89, 14, 4, -78, -1, 2, 7]
Output:
[1, 2, 5]
Input: [1, 2, 3, 4, 5, 6, -7]
Output:
[2, 3, 6]"""


def test(nums):
    import random
    flag = True
    while flag:
        summ = random.choices(nums, k=3)
        if sum(summ) == 0:
            indices = [nums.index(v) for i, v in enumerate(summ)]
            return indices


numbers = [1, 2, 3, 4, 5, 6, -7]
print(test(numbers))

numbers = [12, -7, 3, -89, 14, 4, -78, -1, 2, 7]
print(test(numbers))
