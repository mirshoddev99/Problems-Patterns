"""A string is happy if every three consecutive characters are distinct. Write a
Python program to find two indices making a given string unhappy. Go to the
editor
Input:
Python
Output:
None
Input:
Unhappy
Output:
[4, 5]
Input:
Find
Output:
None
Input:
Street
Output:
[3, 4]"""


def test(strs):
    result = []
    for i in range(len(strs)):
        if strs[i] == strs[i-1]:
            result.append([i-1, i])
    if result:
        return result[0]
    return None


input_str = 'Python'
print(test(input_str))

input_str = 'Street'
print(test(input_str))

input_str = 'Unhappy'
print(test(input_str))
