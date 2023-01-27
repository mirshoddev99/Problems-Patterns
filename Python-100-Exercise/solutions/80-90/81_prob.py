"""Write a Python program to calculate the average of the numbers a through b
( b not included ) rounded to nearest integer, in binary (or -1 if there are no such
numbers). Go to the editor
Input:
4 , 7
Output:
0b101
Input:
11 , 19
Output:
0b1110"""


def test(a, b):
    result = (a + b) // 2

    return bin(result)


print(test(11, 18))
print(test(4, 7))
