"""Write a Python program to find all 5's in integers and its index less than n that are divisible
by 9 or 15. Go to the editor
Input:
Value of n = 50
Output:
[[15, 1], [45, 1]]
Input:
Value of n = 65
Output:
[[15, 1], [45, 1], [54, 0]]
Input:
Value of n = 75
Output:
[[15, 1], [45, 1], [54, 0]]
Input:
Value of n = 85
Output:[[15, 1], [45, 1], [54, 0], [75, 1]]
Input:
Value of n = 150
Output:
[[15, 1], [45, 1], [54, 0], [75, 1], [105, 2], [135, 2]]
"""


def test(n):
    result = []

    for i in range(1, n - 1):
        if i % 9 == 0 or i % 15 == 0:
            number_str = str(i)
            if '5' in number_str:
                result.append([i, number_str.find('5')])

    return result


value_n = 65
print(test((value_n)))

value_n = 150
print(test((value_n)))
