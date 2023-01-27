"""
Write a Python program to find the list of strings that has fewer total
characters (including repetitions). Go to the editor
Input:
[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
Output:
['this', 'list', 'is', 'narrow']
Input:
[['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
Output:
['Red', 'Black', 'Pink']
"""


def test(words):
    return min(words, key=lambda x: sum(len(i) for i in x))


words = [['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
print(test(words))

words = [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
print(test(words))