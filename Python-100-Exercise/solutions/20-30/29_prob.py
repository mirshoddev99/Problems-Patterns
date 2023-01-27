"""
Write a Python program to find the indices of two numbers that sum to 0 in a
given list of numbers. Go to the editor
Input:
[1, -4, 6, 7, 4]
Output:[4, 1]
Input:
[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
Output:
[1, 7]
"""


def test(nums):
    for i in range(len(nums)):
        if -nums[i] in nums:
            return [nums.index(-nums[i]), nums.index(nums[i])]


nums = [1, -4, 6, 7, 4]
print(test(nums))

nums2 = [1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
print(test(nums2))
