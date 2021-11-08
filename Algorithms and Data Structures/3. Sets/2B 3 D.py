n = int(input())
options = set(range(1, n+1))
no = set()
yes = set()
while True:
    s = input()
    if s == 'HELP': break
    b = input()
    tried = set(map(int, s.split()))
    if b == "YES":
        if len(yes) == 0:
            yes = tried
        else:
            yes.intersection_update(tried)
    else: no.update(tried)

if len(yes) > 0:
    options.intersection_update(yes)
options.difference_update(no)
print(*options)
