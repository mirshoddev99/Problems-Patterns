"""Write a Python program to find the vowels from each of the original texts (y
counts as a vowel at the end of the word) from a given list of strings. Go to the
editor
Input: ['w3resource', 'Python', 'Java', 'C++']
Output:
['eoue', 'o', 'aa', '']
Input: ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
Output:
['ay', 'auy', 'aeeay', 'aaey', 'aoeey']"""


def test(words):
    """
    Here is another solution using list comprehension:
    def test(strs):
        return ["".join(c for c in text if c.lower() in "aeiou") + (text[-1] if text[-1].lower() == "y" else "")
            for text in strs]
    """

    s = ""
    result = []
    for i, word in enumerate(words):
        s = ""
        for k in range(len(word)):
            if k == len(word) - 1 and word[k] in 'yY':
                s += word[k]
            elif word[k] in 'oueiaOUEIA':
                s += word[k]
        result.append(s)

    return result


text = ['w3resource', 'Python', 'Java', 'C++']
print(test(text))

text = ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
print(test(text))
