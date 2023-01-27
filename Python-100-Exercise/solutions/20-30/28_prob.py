"""
Write a Python program to select a string from a given list of strings with the
most unique characters. Go to the editor
Input:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Output:
abcdefhijklmnop
Input:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Output:
Orange
"""


def test(words):

    # with lambda
    return max(words, key=lambda x: len(set(x)))

    # max_unique = ""
    # for word in range(len(words) - 1):
    #     if len(set(words[word])) == len(words[word]) and len(words[word]) > len(set(words[word + 1])):
    #         max_unique = words[word]
    # return max_unique
    #

words = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
print(test(words))

words = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
print(test(words))