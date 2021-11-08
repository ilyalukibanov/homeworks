N = int(input())
files = list(map(int, input().split()))
files.sort()
print(sum(files[:N-1]))
