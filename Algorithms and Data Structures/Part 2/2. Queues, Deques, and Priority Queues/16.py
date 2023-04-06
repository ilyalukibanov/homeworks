from collections import deque
with open('input.txt', 'r') as file:
    queue = deque()
    while (s := file.readline().rstrip('\n')) != 'exit':
        if s == 'pop':
            if len(queue) > 0:
                print(queue.popleft())
            else:
                print('error')
        elif s == 'front':
            if len(queue) > 0:
                print(queue[0])
            else:
                print('error')
        elif s == 'size':
            print(len(queue))
        elif s == 'clear':
            queue.clear()
            print('ok')
        else:
            print('ok')
            queue.append(int(s.split()[1]))
    print('bye')