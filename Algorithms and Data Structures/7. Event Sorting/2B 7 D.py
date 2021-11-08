n, m = map(int, input().split())
a = list(map(int, input().split()))
events = []
cats = [0] * m
c = 0
for i in range(m):
    l, r = map(int, input().split())
    events.append((l, -1, c))
    events.append((r, 1, c))
    c += 1
for i in a:
    events.append((i, 0))
cat_count = 0
events.sort()
for event in events:
    if event[1] == 0:
        cat_count += 1
    elif event[1] == -1:
        cats[event[2]] -= cat_count
    elif event[1] == 1:
        cats[event[2]] += cat_count
print(*cats)

