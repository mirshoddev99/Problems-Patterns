"""Write a Python program to round each float in a given list of number up to the
next integer and return the running total of the integer squares. Go to the editor
Input: [2.6, 3.5, 6.7, 2.3, 5.6]
Output:[9, 25, 74, 83, 119]
Input: [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]
Output:
[91204, 252808, 253337, 183714223444221, 183714327525025,
283714327525025]"""


def test(nums):
    import math
    """
    1 step.
    to round each float
    2 step.
    add them together after rounding. append them in a list
    """
    rounded_nums = [math.ceil(x) for x in nums]
    result = []
    for i in range(len(rounded_nums)):
        if i == 0:
            result.append(rounded_nums[i]**2)
        else:
            count = (rounded_nums[i]**2) + result[i - 1]
            result.append(count)
    return result


numbers = [2.6, 3.5, 6.7, 2.3, 5.6]
print(test(nums=numbers))

numbers = [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]
print(test(nums=numbers))