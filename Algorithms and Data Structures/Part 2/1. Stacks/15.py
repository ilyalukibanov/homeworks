N = int(input())
prices = list(map(int, input().split()))
stack = []
new_cities = [-1] * N
for city, price in enumerate(prices):
    while (len(stack) > 0) and (stack[-1][0] > price):
        _, old_city = stack.pop()
        new_cities[old_city] = city
    stack.append((price, city))
print(*new_cities)