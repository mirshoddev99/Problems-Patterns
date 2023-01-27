"""
Write a Python program to find the XOR of two given strings interpreted as
binary numbers. Go to the editor
Input:
[
'0001',
'1011',
'1111'
]
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111
"""


def test(binary):
    return bin(int(binary[0], 2) ^ int(binary[1], 2))


numbers = ['0001', '1011']
print(test(numbers))

numbers = ['100011101100001', '100101100101110']
print(test(numbers))

# Note: (0b) is the prefix that represents of a binary in the result
