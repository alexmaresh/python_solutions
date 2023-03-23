# Implement the function unique_in_order which takes as argument a sequence.
# It returns a list of items without any elements with the same value _next to each other_ and preserving the original order of elements.

# Example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
        unique = []
        last = ''
        for item in sequence:
            if item != last:
                unique.append(item)
                last = item
        return unique