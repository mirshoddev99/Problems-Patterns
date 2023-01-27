"""
Write a Python program to sort numbers based on strings. Go to the editor
Input: six one four one two three
Output:
one two three four six
Input: six one four three two nine eight
Output:
one two three four six eight nine
Input: nine eight seven six five four three two one
Output:
one two three four five six seven eight nine
"""


def test(strs):
    ls = []
    for k in "one two three four five six seven eight nine".split():
        if k in strs:
            ls.append(k)

    return " ".join(ls)


s = "six one four one two three"
print(test(s))

s = "six one four three two nine eight"
print(test(s))
