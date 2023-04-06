r = int(input())
i = int(input())
c = int(input())
if i == 0:
    if r == 0:
        print(c)
    else:
        print(3)
elif i == 1:
    print(c)
elif i == 4:
    if r == 0:
        print(4)
    else:
        print(3)
elif i == 6:
    print(0)
elif i == 7:
    print(1)
else:
    print(i)
