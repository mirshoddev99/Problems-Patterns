"""Given a string consisting of whitespace and groups of matched parentheses,
write a Python program to split it into groups of perfectly matched parentheses without any whitespace. Go to the editor
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']"""


def test(parentheses):
    result = []
    s = ""

    for c in parentheses.replace(" ", ""):
        s += c
        if s.count('(') == s.count(')'):
            result.append(s)
            s = ""

    return result


in_parentheses = '( ()) ((()()())) (()) ()'
print(test(in_parentheses))

in_parentheses = '() (( ( )() ( )) ) ( ())'
print(test(in_parentheses))
