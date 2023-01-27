"""Write a Python program to start with a list of integers, keep every other
element in place and otherwise sort the list. Go to the editor
Input:
[2, 5, 6, 3, 1, 4, 34]
Output:
[1, 5, 2, 3, 6, 4, 34]
Input:
[8, 0, 7, 2, 9, 4, 1, 2, 8, 3]
Output:
[1, 0, 7, 2, 8, 4, 8, 2, 9, 3]"""


def test(nums):
    temp_list = []
    result = []
    for i, v in enumerate(nums):
        if i % 2 == 0:
            print(f"Added into temp_list: {v} \nindex: {i}")
            temp_list.append(v)
        else:
            print(f"Added into result: {v} \nindex: {i}")
            result.append(v)
    temp_list.sort()

    print()
    print("Sorted temp_list: ", temp_list)
    print("Unsorted result_list: ", result)

    result = [temp_list[i // 2] if i % 2 == 0 else result[i // 2] for i in range(len(nums))]

    print(f"\nOriginal list: {nums}")
    return f"Result: {result}"


numbers = [8, 0, 7, 2, 9, 4, 1, 2, 8, 3]
print(test(nums=numbers))

numbers = [2, 5, 6, 3, 1, 4, 34]
print(test(nums=numbers))
