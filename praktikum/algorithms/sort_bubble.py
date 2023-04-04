list = [1,2,35,7,8,5,6,2,0,5,7]

def sort_bubble(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]> l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]

    return l