houses = list(map(int, input().split()))
max_dist = 0
stores = []
for i in range(10):
    if houses[i] == 2: stores.append(i)
for i in range(10):
    if houses[i] == 1:
        lsd = 10
        rsd = 10
        for store in stores:
            if store < i: lsd = i - store
            else:
                rsd = store - i
                break
        max_dist = max(max_dist, min(lsd, rsd))
print(max_dist)

