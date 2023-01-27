# 1. Write a Python program find a list of integers with exactly two occurrences of
# nineteen and at least three occurrences of five. Go to the editor
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input:
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# True

a = [19, 19, 15, 5, 3, 5, 5, 2]
b = [19, 15, 15, 5, 3, 3, 5, 2]
c = [19, 19, 5, 5, 5, 5, 5]

# First solution
def check_num(int_list):
    counter = 0
    for i in range(len(int_list)):
        if int_list[i] == 5 or int_list[i] == 19:
            counter += 1
            if counter >= 5:
                return True

    return False

print(check_num(a))
print(check_num(b))
print(check_num(c))
print('\n')


# Second solution
def check_num_with_method(int_list):
    if (int_list.count(5) + int_list.count(19)) >= 5:
        return True
    return False

print(check_num_with_method(a))
print(check_num_with_method(b))
print(check_num_with_method(c))








