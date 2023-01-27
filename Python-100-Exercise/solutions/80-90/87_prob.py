"""Write a Python program to find a valid substring of a given string that
contains matching brackets, at least one of which is nested. Go to the editor
Input:
]][][[]]]
Output:
[[]]
Input:
]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]] [[[][[][[[ [[][][][]] [[[[[[[[[[[[[[[[[[
Output:
[[][][][]]"""


def matching_brackets(strs):
    import re
    pattern = re.compile(r'\[(\[\])+\]')
    result = re.search(pattern, strs)
    return result.group()


brackets_str = ']][][[]]]'
print(matching_brackets(brackets_str))


brackets_str = ']]]]]]]]]]]]]]]]][][][][]]]]]]]]]]] [[[][[][[[ [[][][][]] [[[[[[[[[[[[[[[[[['
print(matching_brackets(brackets_str))