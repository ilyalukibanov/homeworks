n = int(input())
boxes = {}
for i in range(n):
    d, a = map(int, input().split())
    boxes[d] = a if d not in boxes else boxes[d]+a
for key in sorted(boxes.keys()):
    print(key, ' ', boxes[key])
