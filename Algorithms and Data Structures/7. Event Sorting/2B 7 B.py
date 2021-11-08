n = int(input())
events = []
for i in range(n):
    t, l = map(int, input().split())
    events.append((t, 1))
    events.append((t+l, -1))
events.sort()


current_goods = 0
max_goods = 0
for event in events:
    if event[1] == 1:
        current_goods += 1
    else:
        current_goods -= 1
    max_goods = max(max_goods, current_goods)
print(max_goods)
