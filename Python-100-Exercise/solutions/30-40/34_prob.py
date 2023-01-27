"""
Write a Python program to find the sum of the numbers of a given list among
the first k with more than 2 digits. Go to the editor
Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
Value of K: 4
Output:
0
Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
Value of K: 6
Output:
108
Input: [114, 215, -117, 119, 14, 108, -9, 12, 76]
Value of K: 5
Output:
331
Input: [114, 215, -117, 119, 14, 108, -9, 12, 76]
Value of K: 1
Output:
114
"""


def test(nums, k):
    return sum(nums[i] for i in range(k) if len(str(nums[i])) > 2)


nums = [4, 5, 17, 9, 14, 108, -9, 12, 76]
print(test(nums, 4))

nums = [4, 5, 17, 9, 14, 108, -9, 12, 76]
print(test(nums, 6))

nums = [114, 215, -117, 119, 14, 108, -9, 12, 76]
print(test(nums, 1))

