"""
Write a Python program to compute the sum of the ASCII values of the
upper-case characters in a given string. Go to the editor
Input:
PytHon ExerciSEs
Output:
373
Input:
JavaScript
Output:
157
"""


def test(s):
    summ = 0
    for w in s:
        if w.islower() or w == " ":
            continue
        else:
            summ += ord(w)
    return summ

    # the solution in one line
    # return sum(map(ord,filter(str.isupper,strs)))


string = "PytHon ExerciSEs"
print(test(string))

string = "JavaScript"
print(test(string))
