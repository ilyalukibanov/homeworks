with open('input.txt', 'r') as file:
    N = int(file.readline())
    K = int(file.readline())
    r = int(file.readline())
    s = int(file.readline())
    num = (r-1) * 2 + s
    k = (num-1) % K + 1
    u = num - K
    d = num + K
    print(num,k,u,d)
    ans = ''
    if (u >= 1):
        if d > N:
            ans = 'u'
        else:
            dist_u = r - ((u+1) // 2)
            dist_d = ((d+1) // 2) - r
            if dist_u < dist_d:
                ans = 'u'
            else:
                ans = 'd'
    else:
        if d > N:
            ans = '-1'
        else:
            ans = 'd'
    if ans == 'u':
        print((u+1) // 2, (u+1) % 2 + 1)
    elif ans == 'd':
        print((d+1) // 2, (d+1) % 2 + 1)
    else:
        print(-1)