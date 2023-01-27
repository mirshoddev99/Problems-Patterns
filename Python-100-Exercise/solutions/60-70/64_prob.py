"""
Write a Python program to find the string consisting of all the words whose
lengths are prime numbers. Go to the editor
Input:
The quick brown fox jumps over the lazy dog.
Output:
The quick brown fox jumps the
Input:
Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later.
Output:
Omicron Effect: Foreign Flights Won't On Dec 15,
"""


def isPrime(n: int) -> bool:
    if n == 1 or n == 2:
        return True
    else:
        for i in range(2, n-1):
            if n % i == 0:
                return False
        return True


def test(strs):
    output = ""
    for i in strs.split():
        word_length = len(i)
        if word_length == 1 or word_length == 2:
            output += i + " "
        else:
            if isPrime(word_length) is True:
                output += i + " "

    return output


words = "The quick brown fox jumps over the lazy dog."
print(test(words))

words = "Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later."
print(test(words))


