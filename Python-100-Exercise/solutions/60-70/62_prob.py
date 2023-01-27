"""
Write a Python program to find the dictionary key whose case is different than
all other keys. Go to the editor
Input:
{'red': '', 'GREEN': '', 'blue': 'orange'}
Output:
GREEN
Input:
{'RED': '', 'GREEN': '', 'orange': '#125GD'}
Output:
orange
"""


def test(strs):
    upper_case = []
    lower_case = []
    for k in strs.keys():
        if k.isupper():
            upper_case.append(k)
        else:
            lower_case.append(k)

    if len(lower_case) == 1:
        return lower_case.pop()
    elif len(upper_case) == 1:
        return upper_case.pop()
    else:
        return "There is no different case of the key than all other keys."


strings = {'red': '', 'GREEN': '', 'blue': 'orange'}
print(test(strings))

strings = {'RED': '', 'GREEN': '', 'orange': '#125GD'}
print(test(strings))

strings = {'RED': '', 'GREEN': '', 'orange': '#125GD', 'blue': 'sky'}
print(test(strings))
