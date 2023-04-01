# It is known that the order of notes is as follows: do, re, mi, fa, salt, la, si.
# The input of the program receives a string with a set of these notes, written with a space.
# It is necessary to form a list from the input string with notes sorted in the specified way. Output the result as a string of notes separated by a space.

lst_in = ['do', 'fa', 'salt', 'do', 're', 'fa', 'la', 'si']

a = ['do', 're', 'mi', 'fa', 'salt', 'la', 'si']

print(*sorted(lst_in, key=a.index))
