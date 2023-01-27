"""Given a list of numbers and a number to inject, write a Python program to
create a list containing that number in between each pair of adjacent
numbers. Go to the editor
Input: [12, -7, 3, -89, 14, 88, -78, -1, 2, 7]
Separator: 6
Output:
[12, 6, -7, 6, 3, 6, -89, 6, 14, 6, 88, 6, -78, 6, -1, 6, 2, 6, 7]
Input: [1, 2, 3, 4, 5, 6]
Separator: 9
Output:
[1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6]
"""


def test(nums, separator):
    sol = [separator] * (2 * len(nums) - 1)
    sol[::2] = nums
    return sol

    # second solution
    # result = []
    # for i in range(len(nums)-1):
    #     result.append(nums[i])
    #     result.append(separator)
    #
    # result.append(nums[-1])
    # return result


sep = 9
numbers = [1, 2, 3, 4, 5, 6]
print(test(nums=numbers, separator=sep))

sep = 6
numbers = [12, -7, 3, -89, 14, 88, -78, -1, 2, 7]
print(test(nums=numbers, separator=sep))