"""
3. Write a Python program that accept an integer test whether an integer greater
than 4^4 and which is 4 mod 34.
Input:
922
Output:
True
Input:
914
Output:
False
Input:
854
Output:
True
Input:
854
Output:
True
"""


def check_num(n):
    import math as m
    if n > m.pow(4, 4):
        if n % 34 == 4:
            return True
    return False


n = int(input("Enter integer number: "))
print(check_num(n))
