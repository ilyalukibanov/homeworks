n = int(input())
a = list(map(int, input().split()))
prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + a[i]

max_sum = a[0]
max_index = 0
min_index = 0

for i in range(1, n+1):
    if prefix_sum[i] > prefix_sum[max_index]:
        max_index = i
    elif prefix_sum[i] < prefix_sum[min_index]:
        if min_index != max_index: max_sum = max(max_sum, prefix_sum[max_index] - prefix_sum[min_index])
        min_index = i
        max_index = i
if min_index != max_index: max_sum = max(max_sum, prefix_sum[max_index] - prefix_sum[min_index])
print(max_sum)
