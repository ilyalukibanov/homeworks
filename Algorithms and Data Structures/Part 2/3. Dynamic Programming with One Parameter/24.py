with open('input.txt', 'r') as file:
    N = int(file.readline())
    b1, c1, c2 = float('inf'), float('inf'), float('inf')
    dp1, dp2, dp3 = 0, 0, 0
    for i in range(N):
        a, b, c = map(int, file.readline().split())
        dp = min(dp1+a, dp2+b1, dp3+c2)
        b1, c1, c2 = b, c, c1
        dp3, dp2, dp1 = dp2, dp1, dp
    print(dp)