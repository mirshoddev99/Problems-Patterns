"""Write a Python program to find the two closest distinct numbers in a given a
list of numbers. Go to the editor
Input:
[1.3, 5.24, 0.89, 21.0, 5.27, 1.3]
Output:
[5.24, 5.27]
Input:
[12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]
Output:
[14.99, 15.0]"""


def test(nums):
    closest_val = [0, 1]
    min_distance = float('inf')

    for i in range(len(nums)):
        for k in range(i+1, len(nums)):
            if nums[i] != nums[k]:
                get_distance = abs(nums[i] - nums[k])
                if min_distance > get_distance:
                    min_distance = get_distance
                    closest_val = [nums[i], nums[k]]

    return closest_val


numbers = [12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]
print(test(numbers))