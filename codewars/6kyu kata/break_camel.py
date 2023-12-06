# Complete the solution so that the function will break up camel casing, using a space between words.

def break_camelcase(x):
    res = ""
    for i in x:
        if i.isupper():
            res += " "
        res += i
    return res
