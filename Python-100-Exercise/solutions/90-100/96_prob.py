"""Write a Python program to get the single digits in numbers sorted backwards
and converted to English words. Go to the editor
Input:[1, 3, 4, 5, 11]
Output:
['five', 'four', 'three', 'one']
Input:
[27, 3, 8, 5, 1, 31]
Output:
['eight', 'five', 'three', 'one']"""


def test(nums):
    pattern_dict = {
        "1": "one", "2": "two", "3": "three",
        "4": "four", "5": "five", "6": "six",
        "7": "seven", "8": "eight", "9": "nine"
    }

    result = set(pattern_dict.get(str(v)) for v in sorted(nums, key=lambda x: -x) if str(v) in pattern_dict)
    return result


numbers = [1, 3, 4, 5, 11]
print(test(numbers))

numbers = [27, 3, 8, 5, 1, 31]
print(test(numbers))

numbers = [27, 3, 8, 5, 1, 31, 3, 7, 9]
print(test(numbers))
