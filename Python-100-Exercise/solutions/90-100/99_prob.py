"""Write a Python program to find a string such that, when three or more spaces
are compacted to a '-' and one or two spaces are replaced by underscores, leads
to the target. Go to the editor
Input: Python-Exercises
Output:
Python Exercises
Input: Python_Exercises
Output:
Python Exercises
Input: -Hello,_world!__This_is-so-easy!-
Output:
Hello, world! This is so easy!"""


def test(strs):
    import re
    pattern = re.compile(r'(\_|\-|\__)')
    result = re.sub(pattern, " ", strs)
    return result


input_string = 'Python-Exercises'
print(test(strs=input_string))

input_string = 'Python_Exercises'
print(test(strs=input_string))

input_string = '-Hello,_world!__This_is-so-easy!-'
print(test(strs=input_string))