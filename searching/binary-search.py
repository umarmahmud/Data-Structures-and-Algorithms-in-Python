def binary_search(num, a):
    l = 0
    r = len(a)
    
    while(l < r):
        m = int((l + r)/2)
        if a[m] == num:
            return m
        elif a[m] > num:
            r = m - 1
        elif a[m] < num:
            l = m + 1
    return -1
