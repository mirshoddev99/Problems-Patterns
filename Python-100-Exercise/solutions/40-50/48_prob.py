"""Write a Python program to find the indices of two entries that show that the
list is not in increasing order. If there are no violations (they are increasing),
return an empty list. Go to the editor
Input:
[1, 2, 3, 0, 4, 5, 6]
Output:
[2, 3]
Input:
[1, 2, 3, 4, 5, 6]
Output:
[]
Input:
[1, 2, 3, 4, 6, 5, 7]
Output:
[4, 5]
Input:
[-3, -2, -3, 0, 2, 3, 4]
Output:
[1, 2]"""


def test(nums):

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return [i, i+1]

    return []


nums = [-3, -2, -3, 0, 2, 3, 4]
print(test(nums))

nums = [1, 2, 3, 4, 6, 5, 7]
print(test(nums))

nums = [1, 2, 3, 4, 5, 6]
print(test(nums))

nums = [1, 2, 3, 0, 4, 5, 6]
print(test(nums))