x, y, z = map(int, input().split())
if y > 12 or x > 12: print(1)
elif x == y and x <= 12: print(1)
else: print(0)
