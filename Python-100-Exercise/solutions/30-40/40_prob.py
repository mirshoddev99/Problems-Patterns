"""
Write a Python program to find string s that, when case is flipped gives target
where vowels are replaced by chars two later. Go to the editor
Input: Python
Output:
pYTHQN
Input: aeiou
Output:
CGKQW
Input: Hello, world!
Output:
hGLLQ, WQRLD!
Input: AEIOU
Output:
cgkqw
"""


# def test(strs):
#     return strs.translate({ord(c): ord(c) + 2 for c in "aeiouAEIOU"}).swapcase()
#
#
# strs = "Python"
# print("Original string:", strs)
# print("Find string s that, when case is flipped gives target where vowels are replaced by chars two later:")
# print(test(strs))

def test(word):
    new_string = ""
    for w in word:
        if w.islower() and w in ['a', 'e', 'u', 'i', 'o']:
            new_string += chr(ord(w) - 30)

        elif w.isupper() and w in ['A', 'E', 'U', 'i', 'o']:
            new_string += chr(ord(w) + 34)

        elif w not in ['A', 'E', 'U', 'I', 'O'] or w not in ['a', 'e', 'u', 'i', 'o']:
            if w.islower():
                new_string += w.upper()
            else:
                new_string += w.lower()

    return new_string


input_str = "Python"
print(test(input_str))

input_str = "Hello, world!"
print(test(input_str))


"""                 ..........Reference.......... 

The original ASCII represents 128 characters in decimal numbers. Each of these 
characters (letters of the English alphabet, numbers and various punctuation marks) are assigned a decimal number 
from 0 to 127. For example, the ASCII representation for uppercase A is 65 and lower case a is 97. 

The each character of the ASCII has its decimal value in the ASCII table. 
The decimal value of Upper cases is 32 times lower than the decimal value of Lower cases.
"""
