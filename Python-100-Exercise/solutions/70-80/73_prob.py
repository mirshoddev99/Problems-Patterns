"""Write a Python program to find a substring in a given string contains a vowel
between two consonants. Go to the editor
Input: Hello
Output:
Hel
Input: Sandwhich
Output:
San
Input: Python
Output:
hon"""


def test(strs):
    result = ""
    for v in range(1, len(strs)-1):
        if (strs[v-1] not in 'AEIOUaeiou' and strs[v+1] not in 'AEIOUaeiou') and strs[v] in 'AEIOUaeiou':
            result += strs[v-1:v+2]
            return result


in_strs = "Hello"
print(test(in_strs))

in_strs = "Sandwhich"
print(test(in_strs))

in_strs = "Python"
print(test(in_strs))