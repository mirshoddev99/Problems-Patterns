"""
Write a Python program to check whether the given strings are palindromes
or not. Return True, False. Go to the editor
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]
"""


def test(words):
    ls_words = ['True' if w == w[::-1] else 'False' for w in words]
    return ls_words


word_list = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
print(test(word_list))

word_list = ['lola', 'hello', '', 'aziza', 'abba']
print(test(word_list))

