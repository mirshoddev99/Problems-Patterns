"""Write a Python program to find the indices of the closest pair from a list of
numbers. Go to the editor
Input: [1, 7, 9, 2, 10]
Output:
[0, 3]
Input: [1.1, 4.25, 0.79, 1.0, 4.23]
Output:
[4, 1]
Input: [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]
Output:
[2, 5]
"""


def test(numbers):
    min_distance = float('inf')
    pairs = [0, 1]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < min_distance:
                min_distance = distance
                pairs = [i, j]
    return pairs


nums = [1, 7, 9, 2, 10]
print(test(nums))

nums = [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]
print(test(nums))
