"""Write a Python program to find the following strange sort of list of numbers:
the first element is the smallest, the second is the largest of the remaining, the
third is the smallest of the remaining, the fourth is the smallest of the remaining,
etc. Go to the editor
Input:
[1, 3, 4, 5, 11]
Output:
[1, 11, 3, 5, 4]
Input:
[27, 3, 8, 5, 1, 31]
Output:
[1, 31, 3, 27, 5, 8]
Input:
[1, 2, 7, 3, 4, 5, 6]
Output:
[1, 7, 2, 6, 3, 5, 4]"""


def test(nums):
    result = []

    while nums:
        result.append(min(nums))
        nums.remove(min(nums))
        if nums:
            result.append(max(nums))
            nums.remove(max(nums))

    return result


numbers = [1, 2, 7, 3, 4, 5, 6]
print(test(numbers))

numbers = [27, 3, 8, 5, 1, 31]
print(test(numbers))

