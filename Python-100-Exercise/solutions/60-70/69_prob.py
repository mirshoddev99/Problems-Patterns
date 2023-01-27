"""Write a Python program to create a new string by taking a string, and word by
word rearranging its characters in ASCII order. Go to the editor
Input: Ascii character table
Output:
Aciis aaccehrrt abelt
Input: maltos won
Output:
almost now"""


def test(strs):
    return " ".join("".join(sorted(w)) for w in strs.split())


input_str = 'Ascii character table'
print(test(input_str))

input_str = 'maltos won'
print(test(input_str))
