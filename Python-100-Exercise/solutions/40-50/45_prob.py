"""
Write a Python program to find all even palindromes up to n. Go to the editor
Output:Even palindromes up to 50 -
[0, 2, 4, 6, 8, 22, 44]
Even palindromes up to 100 -
[0, 2, 4, 6, 8, 22, 44, 66, 88]
Even palindromes up to 500 -
[0, 2, 4, 6, 8, 22, 44, 66, 88, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292,
404, 414, 424, 434, 444, 454, 464, 474, 484, 494]
Even palindromes up to 2000 -
[0, 2, 4, 6, 8, 22, 44, 66, 88, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292,
404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 606, 616, 626, 636, 646, 656,
666, 676, 686, 696, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898]
"""


def test(n):
    return [k for k in range(0, n+1, 2) if str(k) == str(k)[::-1]]


n = 50
print(test(n))

n = 100
print(test(n))

n = 500
print(test(n))

n = 2000
print(test(n))
