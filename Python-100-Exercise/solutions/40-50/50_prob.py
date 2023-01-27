""" Write a Python program to find the even-length words from a given list of
words and sort them by length. Go to the editor
Original list of words:
['Red', 'Black', 'White', 'Green', 'Pink', 'Orange']
Find the even-length words and sort them by length in the said list of words:
['Pink', 'Orange']
Original list of words:
['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']
Find the even-length words and sort them by length in the said list of words:
['!!', 'bird', 'that', 'worm', 'Absurd']"""


def test(strs):

    # it is easier to read
    filtered = filter(lambda w: len(w) % 2 == 0, strs)
    return sorted(filtered, key=lambda x: len(x))

    # it is more complicated to read
    # return sorted(filter(lambda w: len(w) % 2 == 0, strs), key=lambda x: len(x))


strs = ['Red', 'Black', 'White', 'Green', 'Pink', 'Orange']
print(test(strs))

strs = ['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']
print(test(strs))

strs = ['mir', 'john', 'doe', '!!']
print(test(strs))