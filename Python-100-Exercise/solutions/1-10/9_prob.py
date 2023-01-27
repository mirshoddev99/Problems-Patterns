"""
9. Write a Python program to find list integers containing exactly four distinct
values, such that no integer repeats twice consecutively among the first twenty
entries. Go to the editor
Input:
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Output:
True
Input:
[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
Output:
False
Input:
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
Output:
False
"""

def check_n(nums):
    count = 0
    if len(set(nums)) == 4:
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                print(f"i = {i} nums[{nums[i]}] != nums[{nums[i+1]}]\n")
                count += 1
        if count >= 4:
            print(f"Count {count}\n")
            return True
    return False


n = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(check_n(n))

n = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
print(check_n(n))

n = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(check_n(n))