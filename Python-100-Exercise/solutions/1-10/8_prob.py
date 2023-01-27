"""
Write a Python program to split a string of words separated by commas and
spaces into two lists, words and separators. Go to the editor
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
Input: The dance, held in the school gym, ended at midnight.
Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'],
[' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
Input: The colors in my studyroom are blue, green, and yellow.
Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ',
' ', ' ', ' ', ', ', ', ', ' ']]

"""


def check_str(st):
    res1 = "".join(st.split(',')).split()
    res2 = []
    for x in st:
        if x not in ''.join(res1):
            res2.append(x)

    res3 = []
    for i in range(len(res2)):
        if res2[i] == ',' and res2[i + 1] == ' ':
            res3.append(res2[i] + res2[i + 1])

        elif res2[i - 1] != ',':
            res3.append(res2[i])
    result = [res1 ,res3]
    return result


text = 'W3resource Python, Exercises.'
print(f"{check_str(text)}\n")

text = 'The dance, held in the school gym, ended at midnight.'
print(f"{check_str(text)}\n")

text = 'The colors in my studyroom are blue, green, and yellow.'
print(f"{check_str(text)}\n")



