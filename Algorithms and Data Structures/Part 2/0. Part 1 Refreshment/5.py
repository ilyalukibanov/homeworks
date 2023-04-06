N = int(input())
n_letters = []
answer = 0
last = 0
for i in range(N):
    current = int(input())
    answer += (min(current, last))
    last = current
print(answer)