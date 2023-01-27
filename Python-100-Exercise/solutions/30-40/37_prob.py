"""
Write a Python program to find the largest integer divisor of a number n that
is less than n. Go to the editor
Input: 18
Output:9
Input: 100
Output:
50
Input: 102
Output:
51
Input: 500
Output:
250
Input: 1000
Output:
500
Input: 6500
Output:
3250
"""


def test(n):
    return max(i for i in range(n-1, 1, -1) if n % i == 0)


n = 18
print(test(n))

n = 6500
print(test(n))

n = 1000
print(test(n))

n = 102
print(test(n))

n = 15
print(test(n))