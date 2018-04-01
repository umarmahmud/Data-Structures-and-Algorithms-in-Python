def linear_search(num, a):
    for i in range(len(a)):
        if a[i] == num:
            return i
    return -1