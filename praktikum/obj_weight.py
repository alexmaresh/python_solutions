# The weights of the items are given as str.
# # It is necessary to form a dictionary on the basis of these data and, then, on the basis of this dictionary, form a list of items in descending order of their weight.
# Display the result as a string with names separated by a space.

lst_in = ['scissors=100', 'pot=500', 'matches=20', 'lighter=40', 'mirror=50']


def sort_by_weight(lst_in:list):
    dict_in = {}
    for i in lst_in:
        res = i.split('=')
        dict_in[res[0]]=int(res[1])

    res = sorted(dict_in, key=lambda item: dict_in[item], reverse=True)
    return res
