"""Write a Python program to find all integers <= 1000 that are the product of
exactly three primes. Each integer should represent as the list of its three prime
factors. Go to the editor
Input: 10
Output:
[[2, 2, 2]]
Input: 50
Output:
[[2, 2, 2], [2, 2, 3], [2, 2, 5], [2, 2, 7], [2, 2, 11], [2, 3, 2], [2, 3, 3], [2, 3, 5], [2, 3, 7],
[2, 5, 2], [2, 5, 3], [2, 5, 5], [2, 7, 2], [2, 7, 3], [2, 11, 2], [3, 2, 2], [3, 2, 3], [3, 2, 5],
[3, 2, 7], [3, 3, 2], [3, 3, 3], [3, 3, 5], [3, 5, 2], [3, 5, 3], [3, 7, 2], [5, 2, 2], [5, 2, 3],
[5, 2, 5], [5, 3, 2], [5, 3, 3], [5, 5, 2], [7, 2, 2], [7, 2, 3], [7, 3, 2], [11, 2, 2]]"""


def test(n):
    """
    Steps:
    1. select three numbers from the prime numbers list
    2. check if i is equal to product of three prime numbers if it is, append that three prime numbers in the result list
    """
    triplets = []
    prime_nums = []
    for i in range(2, n + 1):
        isPrime = True
        for k in range(2, int(i ** 0.5) + 1):
            if i % k == 0:
                isPrime = False
                break
        if isPrime:
            prime_nums.append(i)

    for i in range(8, n + 1):
        for j in prime_nums:
            for s in prime_nums:
                for a in prime_nums:
                    if i == j * s * a:
                        triplets.append([j, s, a])

    # print(len(triplets))
    return triplets


print(test(n=10))
print(test(n=50))
