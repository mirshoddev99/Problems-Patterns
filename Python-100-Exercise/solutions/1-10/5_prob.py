"""5. Write a Python program to check the nth-1 string is a proper substring of
nth string in a given list of strings. Go to the editor
Input:
['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
Output:
True
Input:
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
Output:
True"""


def check_substring(s):
    prev = s[-2]
    last = s[-1]

    if prev in last and len(prev) != len(last):
        return True
    return False


print(check_substring(['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
print(check_substring(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']))
print(check_substring(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']))
print(check_substring(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']))