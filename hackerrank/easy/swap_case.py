# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.
#Example: Www.HackerRank.com → wWW.hACKERrANK.COM

def swap(s):
    new_s = ""
    for i in s:
        print(i)
        if i.islower():
            new_s+=i.upper()
        elif i.isupper():
            new_s+=i.lower()
        else:
            new_s+=i
    return new_s


