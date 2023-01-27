""" Write a Python program to find the closest palindrome from a given string. Go
to the editor
Input:
cat
Output:
cac
Input:
madan
Output:
madam
Input:
radivider
Output:
radividar
"""


def closest_palindrome(s):
    count = 0
    for idx, char in enumerate(s):
        if char != s[~idx]:
            count += 1
    if count % 2 == 1:
        half = count // 2
        return "".join((s[half] if i < half else s[~i] for i in range(len(s))))
    else:
        half = count // 2
        return "".join((s[i] if i <= half else s[~i] for i in range(len(s))))


strs = 'madan'
# strs = 'nadam'
result = closest_palindrome(s=strs)
print(result)

# strs = 'radivider'
# result = closest_palindrome(s=strs)
# print(result)
#
# strs = 'azizaasisa'
# # strs = 'asisaaziza'
# result = closest_palindrome(s=strs)
# print(result)
