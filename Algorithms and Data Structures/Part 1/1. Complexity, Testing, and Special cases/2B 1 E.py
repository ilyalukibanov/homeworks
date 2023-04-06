d = int(input())
x, y = map(int, input().split())
hd = d/2
if x >= 0 and y >= 0 and (x + y <= d): print(0)
elif (x < 0 and y <= hd) or (y < 0 and x <= hd): print(1)
elif y < 0 or (y >= 0 and x-y>=0): print(2)
else: print(3)
