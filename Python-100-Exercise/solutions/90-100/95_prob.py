"""Write a Python program to find a palindrome of a given length containing a
given string. Go to the editor
Input: madam , 7
Output:
madaadam
Input: madam , 6
Output:
maddam
Input: madam , 5
Output:
maaaam
Input: madam , 3
Output:
maam
Input: madam , 2
Output:
mm
Input: madam , 1
Output:
aa"""


def test(s, n):
    from random import choices
    container = " ".join(s).split()

    while True:
        result = "".join(choices(container, k=n+1))
        if result == result[::-1]:
            return f"Output: {result}"

s = 'madam'
n = 7
print(test(s, n))

s = 'madam'
n = 6
print(test(s, n))

s = 'madam'
n = 5
print(test(s, n))

s = 'madam'
n = 4
print(test(s, n))

s = 'madam'
n = 3
print(test(s, n))
