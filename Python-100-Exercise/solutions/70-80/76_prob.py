"""Write a Python program to find the index of the largest prime in the list and
the sum of its digits. Go to the editor
Input: [3, 7, 4]
Output:
[1, 7]
Input: [3, 11, 7, 17, 19, 4]
Output:
[4, 10]
Input: [23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]
Output:
[6, 7]"""


def isPrime(nums):
    for i in range(len(nums)):
        max_num = max(nums)
        for k in range(2, int(max_num ** 0.5) + 1):
            if max_num % k == 0:
                break
        else:
            return max_num
    return False


def test(primes):
    max_num = isPrime(primes)
    if max_num is not False:
        if len(str(max_num)) == 1:
            return [primes.index(max_num), max_num]
        else:
            cnt_list = list(map(lambda x: int(x), str(max_num)))
            return [primes.index(max_num), sum(cnt_list)]


input_nums = [3, 11, 7, 17, 19, 4]
print(test(input_nums))

input_nums = [3, 7, 4]
print(test(input_nums))

input_nums = [3, 7, 4, 13, 31]
print(test(input_nums))
