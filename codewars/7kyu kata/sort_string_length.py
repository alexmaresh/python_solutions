# Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.
# For example, if this array were passed as an argument:
# ["Telescopes", "Glasses", "Eyes", "Monocles"]
# Your function would return the following array:
# ["Eyes", "Glasses", "Monocles", "Telescopes"]
# All of the strings in the array passed to your function will be different lengths, so you will not have to decide how to order multiple strings of the same length.

# bubble_sort
def sort_by_length(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# simple
def sort_by_length(arr):
    return sorted(arr, key=len)
