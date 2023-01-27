"""
Write a Python program to find the first n Fibonacci numbers. Go to the editor
Input: 10
Output:
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
Input: 15
Output:
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
Input: 50
Output:
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
39088169, 63245986, 102334155, 165580141, 267914296, 433494437,
701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049,
12586269025]
"""


def test(fibo):
    a, b = 1, 1

    while 0 < fibo:
        yield a
        a, b = b, a + b
        fibo -= 1


    # second solution
    # a = [1, 1]
    # while len(a) < fibo:
    #     a.extend([sum(a[-2:])])
    #
    # return a


fib = 10
my_fibo_nums = list(test(fib))
print(my_fibo_nums)

fib = 15
my_fibo_nums = list(test(fib))
print(my_fibo_nums)

fib = 50
my_fibo_nums = list(test(fib))
print(my_fibo_nums)