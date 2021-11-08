s = input()
isRight = True
delta = 0
for i in range(len(s)):
    if s[i] == '(': delta += 1
    else: delta -= 1
    if delta < 0: isRight = False
if delta > 0: isRight = False
if isRight: print('YES')
else: print("NO")
