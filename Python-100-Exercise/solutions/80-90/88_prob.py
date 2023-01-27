"""Write a Python program to find an integer (n >= 0) with the given number of
even and odd digits. Go to the editor
Input:
Number of even digits: 2 ,Number of odd digits: 3
Output:
22333
Input:
Number of even digits: 4 ,Number of odd digits: 7
Output:
22223333333"""


def test(even, odd):
    n = even * '2' + odd * '3'
    return n


print(test(4, 7))
print(test(2, 3))
