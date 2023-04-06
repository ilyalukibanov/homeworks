L, K = map(int, input().split())
blocks = list(map(int, input().split()))
n = len(blocks)
hl = L // 2 - 1
if L % 2 == 1:
    try:
        blocks.index(L // 2)
        print(L // 2)
    except ValueError:
        for i in range(n):
            if blocks[i] > hl:
                print(blocks[i-1], blocks[i])
                break
else:
    for i in range(n):
        if blocks[i] > hl:
            print(blocks[i - 1], blocks[i])
            break
