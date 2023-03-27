# Return two indexes with the highest values that are consecutive

lst = [1,2,3,6,66,77,99]

def find_pair_idx(lst):
    max_sum = 0
    f_idx = None
    s_idx = None

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            cur_sum = lst[i] + lst[j]
            if cur_sum > max_sum:
                max_sum = cur_sum
                f_idx = i
                s_idx = j

    return (f_idx,s_idx)
