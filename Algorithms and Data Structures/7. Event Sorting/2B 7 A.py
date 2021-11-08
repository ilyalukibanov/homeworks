n = int(input())
events = []
for i in range(n):
    l, r = map(int, input().split())
    events.append((l, -1))
    events.append((r, 1))
events.sort()

length = 0
n_lines = 0
left = 0
for event in events:
    if n_lines == 0:
        left = event[0]
    if event[1] == 1:
        n_lines += 1
    else:
        n_lines -= 1
    if n_lines == 0:
        length += event[0] - left
print(length)
