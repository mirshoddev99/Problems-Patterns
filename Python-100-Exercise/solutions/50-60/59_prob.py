"""
A valid filename should end in .txt, .exe, .jpg, .png, or .dll, and should have at
most three digits, no additional periods. Write a Python program to create a list of
True/False that determine whether candidate filename is valid or not. Go to the
editor

Input:
['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
Output:
['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes']

Input:
['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']
Output:
['No', 'Yes', 'No', 'No', 'No']
"""


def test(f):
    """
    valid types of filename
    .txt
    .dll
    .png
    .jpg
    .exe
    """

    return ["Yes" if i[0].isalpha() and i[-4:] in [".txt", ".dll", ".png", ".jpg", ".exe"] else "No" for i in f]


f_names = ['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
print(test(f_names))

f_names = ['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']
print(test(f_names))

