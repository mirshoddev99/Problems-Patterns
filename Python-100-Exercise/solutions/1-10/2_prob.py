# 2. Write a Python program that accept a list of integers and check the length and
# the fifth element. Return true if the length of the list is 8 and fifth element occurs
# thrice in the said list. Go to the editor
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True
# Input:
# [19, 15, 5, 7, 5, 5, 2]
# Output:False
# Input:
# [11, 12, 14, 13, 14, 13, 15, 14]
# Output:
# True
# Input:
# [19, 15, 11, 7, 5, 6, 2]
# Output:
# False

def length_of_list(list_length):
    if len(list_length) < 8:
        return False
    elif len(list_length) >= 8:
        if list_length.count(list_length[4]) >= 3:
            return True
    return False


print(length_of_list([19, 19, 15, 5, 5, 5, 1, 2]))
print(length_of_list([19, 15, 5, 7, 5, 5, 2]))
print(length_of_list([11, 12, 14, 13, 14, 13, 15, 14]))
print(length_of_list([19, 15, 11, 7, 5, 6, 2]))
