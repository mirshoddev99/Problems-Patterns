"""Write a Python program to find the largest negative and smallest positive
numbers (or 0 if none). Go to the editor
Input:
[-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
Output:
[-6, 2]
Input:
[-1, -2, -3, -4]
Output:
[-1, 0]
Input:
[1, 2, 3, 4]
Output:
[0, 1]
Input:
[]
Output:
[0, 0]"""


def test(nums):
    if nums:
        if all(i > 0 for i in nums):
            smallest_pos = min(x for x in nums if x > 0)
            return [0, smallest_pos]
        elif all(i < 0 for i in nums):
            largest_neg = max(x for x in nums if x < 0)
            return [largest_neg, 0]
        else:
            smallest_pos = min(x for x in nums if x > 0)
            largest_neg = max(x for x in nums if x < 0)
            return [largest_neg, smallest_pos]
    else:
        return [0, 0]


numbers = [-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
print(test(nums=numbers))

numbers = [-1, -2, -3, -4]
print(test(nums=numbers))
