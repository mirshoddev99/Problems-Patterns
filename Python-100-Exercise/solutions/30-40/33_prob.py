"""
Write a Python program to find the positions of all uppercase vowels (not
counting Y) in even indices of a given string. Go to the editor
Input: w3rEsOUrcE
Output:
[6]
Input: AEIOUYW
Output:
[0, 2, 4]
"""


def test(s):
    return [idx for idx, w in enumerate(s) if w in ["A", "E", "I", "O", "U"] and idx % 2 == 0]


string = "w3rEsOUrcE"
print(test(string))

string = "AEIOUYW"
print(test(string))
