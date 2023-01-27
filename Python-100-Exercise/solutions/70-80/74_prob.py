"""Write a Python program to find a string consisting of space-separated
characters with given counts. Go to the editor
Input: {'f': 1, 'o': 2}
Output:
f o o
Input: {'a': 1, 'b': 1, 'c': 1}
Output:
a b c"""


def test(counts):
    return " ".join(k*v for k, v in counts.items())


in_str = {'a': 1, 'b': 1, 'c': 1}
print(test(in_str))

in_str = {'f': 1, 'o': 2}
print(test(in_str))
