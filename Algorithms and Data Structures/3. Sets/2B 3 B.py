numbers = list(map(int, input().split()))
unique = set()
for num in numbers:
    if num in unique:
        print('YES')
    else:
        unique.add(num)
        print('NO')
