"""Write a Python program to find a list of all numbers that are adjacent to a
prime number in the list, sorted without duplicates. Go to the editor
Input:
[2, 17, 16, 0, 6, 4, 5]
Output:
[2, 4, 16, 17]
Input:
[1, 2, 19, 16, 6, 4, 10]
Output:
[1, 2, 16, 19]
Input:
[1, 2, 3, 5, 1, 16, 7, 11, 4]
Output:
[1, 2, 3, 4, 5, 7, 11, 16]"""


def test(nums):
    return sorted({
        n for i, n in enumerate(nums)
        if (i > 0 and prime(nums[i - 1])) or (i < len(nums) - 1 and prime(nums[i + 1]))
    })


def prime(m):
    if m > 0:
        return all(m % i for i in range(2, m - 1))


nums = [2, 17, 16, 0, 6, 4, 5]
print(test(nums))


nums = [1, 2, 3, 5, 1, 16, 7, 11, 4]
print(test(nums))
