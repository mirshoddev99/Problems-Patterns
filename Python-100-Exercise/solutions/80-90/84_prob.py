"""Write a Python program to find the index of the matching parentheses for
each character in a given string. Go to the editor
Input: ()(())
Output:
[1, 0, 5, 4, 3, 2]
Input: ()()()
Output:
[1, 0, 3, 2, 5, 4]
Input: ((()))
Output:
[5, 4, 3, 2, 1, 0]"""


def find_matching_parens(brackets):
    indices = [-1 for _ in range(len(brackets))]
    stack = []
    for i, char in enumerate(brackets):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                indices[i] = stack.pop()
                indices[indices[i]] = i
    return indices


parens = "()()()"
print(find_matching_parens(parens))

parens = "(())"
print(find_matching_parens(parens))

parens = "((()))"
print(find_matching_parens(parens))
