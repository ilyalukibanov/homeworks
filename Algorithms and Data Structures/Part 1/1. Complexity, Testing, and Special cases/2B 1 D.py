N = int(input())
dist = list(map(int, input().split()))
rs = sum(dist) - N * dist[0]
s = 0
md = rs+1
ind = 0
for i in range(N-1):
    d = dist[i+1] - dist[i]
    s += d * (i+1)
    rs -= d * (N-i-1)
    # print(s, 's')
    # print(rs, 'rs')
    if rs+s < md:
        md = rs+s
        ind = i+1
print(dist[ind])
