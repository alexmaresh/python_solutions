# In some country banknotes are used in denominations of 1, 2, 4, 8, 16, 32 and 64.
# A natural number n is entered.
# How can the sum n be paid with the least amount of such banknotes?
# Display a list of banknotes to form the sum n (in one line separated by a space, starting with the largest and ending with the smallest).
# It is assumed that there is a sufficiently large number of banknotes of all denominations.
banknotes = [1,2,4,8,16,32,64]
n = 221
def banknotes_count(b,n):
    banknotes = sorted(b, reverse=True)
    res = []
    remain = n
    for b in banknotes:
        if b <= remain:
            count = remain//b
            res += [b]*count
            remain -=b*count
    return res


