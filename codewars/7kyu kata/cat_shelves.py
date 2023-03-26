# An infinite number of shelves are arranged one above the other in a staggered fashion.
# The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3
# Find the minimum number of jumps to go from start to finish

def solution(start, finish):
    n = finish - start
    return n // 3 + n % 3
