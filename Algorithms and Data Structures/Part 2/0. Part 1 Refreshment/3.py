def find_number(l, r, unique_stamps, value):
    while l < r:
        m = (l+r) // 2
        if unique_stamps[m] > value-1:
            r = m
        else:
            l = m+1
    return l


with open('input.txt', 'r') as file:
    N = int(file.readline())
    unique_stamps = list(set(map(int, file.readline().split())))
    K = int(file.readline())
    ps = list(map(int, file.readline().split()))
    unique_stamps.sort()
    n_unique_stamps = len(unique_stamps)
    for p in ps:
        print(find_number(0, n_unique_stamps, unique_stamps, p))