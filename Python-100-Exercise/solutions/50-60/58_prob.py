"""Write a Python program to find the biggest even number between two
numbers inclusive. Go to the editor
Input:
m = 12
n = 51
Output:
50
Input:
m = 1
n = 79
Output:
78
Input:
m = 47
n = 53
Output:
52
Input:
m = 100
n = 200
Output:
200"""


def test(m, n):
    if n > m:
        if n & 1:
            return n - 1
        else:
            return n
    elif m < n:
        if m & 1:
            return m - 1
        else:
            return m


m = 12
n = 51
print(test(m, n))

m = 1
n = 79
print(test(m, n))

m = 100
n = 200
print(test(m, n))
