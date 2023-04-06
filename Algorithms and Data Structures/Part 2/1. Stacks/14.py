n = int(input())
railcars = list(map(int, input().split()))
stack = []
is_doable = 'YES'
last_sorted = 0
for railcar in railcars:
    if railcar == last_sorted+1:
        last_sorted += 1
        if not stack:
            continue
        to_move = stack.pop()
        while to_move == last_sorted+1:
            last_sorted += 1
            if len(stack) == 0:
                break
            to_move = stack.pop()
        if to_move > last_sorted:
            stack.append(to_move)
    elif (len(stack) > 0) and (railcar > stack[-1]):
        is_doable = 'NO'
        break
    else:
        stack.append(railcar)
print(is_doable)