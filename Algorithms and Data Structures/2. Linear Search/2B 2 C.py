s = input()
n = len(s)
c = 0
if n > 1:
    for i in range(n // 2):
        if s[i] != s[~i]: c += 1
print(c)

