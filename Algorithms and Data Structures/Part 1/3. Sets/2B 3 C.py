numbers = list(map(int, input().split()))
unique = []
two_plus = set()
for num in numbers:
    if num in two_plus: pass
    elif num in unique:
        unique.remove(num)
        two_plus.add(num)
    else: unique.append(num)
print(*unique)
