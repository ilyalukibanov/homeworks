K = int(input())
min_x = 1_000_000_000
min_y = 1_000_000_000
max_x = -1_000_000_000
max_y = -1_000_000_000
for i in range(K):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
print(min_x, min_y, max_x, max_y)

