"""
Write a Python program to reverse the case of all strings. For those strings,
which contain no letters, reverse the strings. Go to the editor
Original list:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Reverse the case of all strings. For those strings which contain no letters,
reverse the strings:
['CAT', 'CATATATATCTSA', 'ABCDEFHIJKLMNOP', '521581932952421', '',
'FOO', 'UNIQUE']
Original list:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Reverse the case of all strings. For those strings which contain no letters,
reverse the strings:
['gREEN', 'rED', 'oRANGE', 'yELLOW', '', 'wHITE']
Original list:
['Hello', '!@#', '!@#$', '123#@!']
Reverse the case of all strings. For those strings which contain no letters,
reverse the strings:
['hELLO', '#@!', '$#@!', '!@#321']
"""


def test(strs):
    return [x[::-1] if x.isalpha() is not True else x for x in strs]


strs = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
print(test(strs))

strs = ['Hello', '!@#', '!@#$', '123#@!']
print(test(strs))