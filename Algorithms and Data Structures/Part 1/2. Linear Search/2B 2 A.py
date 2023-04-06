ans = 0
mn = 0
while True:
    num = int(input())
    if num > mn:
        ans = 1
        mn = num
    elif num == mn:
        ans += 1
    elif num == 0: break
print(ans)
