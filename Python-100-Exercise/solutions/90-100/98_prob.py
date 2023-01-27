"""Given a string consisting of groups of matched nested parentheses
separated by parentheses, write a Python program to compute the depth of each
group. Go to the editor
Input: (()) (()) () ((()()()))
Output:
[2, 2, 1, 3]
Input: () (()) () () () ()
Output:
[1, 2, 1, 1, 1, 1]
Input: (((((((()))))))) () (()) ((()()()))
Output:
[8, 1, 2, 3]"""


def count_matching_parentheses(s):
    depth = 0
    max_depth = 0
    result = []
    for c in s:
        if c == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif c == ')':
            if depth > 0:
                depth -= 1
                if depth == 0:
                    result.append(max_depth)
                    max_depth = 0
            else:
                return "Error: Unbalanced parentheses"

    if depth != 0:
        return "Error: Unbalanced parentheses"
    return f"Output: {result}"


input_str = '(()) (()) () ((()()()))'
result = count_matching_parentheses(input_str)
print(result)

input_str = '(((((((()))))))) () (()) ((()()()))'
result = count_matching_parentheses(input_str)
print(result)


