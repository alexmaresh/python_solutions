# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
# ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
# Please note that using encode is considered cheating.
import string

def rot13(message):
    l = string.ascii_lowercase
    u = string.ascii_uppercase
    res = ''
    for i in message:
        rot_dict = u if i.isupper() else l
        if not i.isalpha():
            res += str(i)

        if i.isalpha():
            idx = (rot_dict.index(i)) + 13

            if idx >= 26:
                new_idx = abs(26 - idx)
                res += (rot_dict[new_idx])
            if idx < 26:
                res += (rot_dict[idx])
    return res
