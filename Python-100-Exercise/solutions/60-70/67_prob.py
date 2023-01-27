"""Write a Python program to find a string which, when each character is shifted
(ASCII incremented) by shift, gives the result. Go to the editor
Input:
Ascii character table
Shift = 1
Output:
@rbhhbg`q`bsdqs`akd
Input:
Ascii character table
Shift = -1
Output:
Btdjj!dibsbdufs!ubcmf"""


def test(strs, shift):
    shifted_strs = ""

    for s in strs:
        get_ascii_code = ord(s)
        shift_it = get_ascii_code - shift
        shifted_strs += chr(shift_it)

    return shifted_strs


input_str = 'Ascii character table'
shift = 1
print(test(input_str, shift))

input_str = 'Ascii character table'
shift = -1
print(test(input_str, shift))