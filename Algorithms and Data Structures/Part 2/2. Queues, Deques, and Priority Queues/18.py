from collections import deque
with open('input.txt', 'r') as file:
    deque_ = deque()
    while (s := file.readline().rstrip('\n')) != 'exit':
        if s == 'pop_front':
            if len(deque_) > 0:
                print(deque_.popleft())
            else:
                print('error')
        elif s == 'pop_back':
            if len(deque_) > 0:
                print(deque_.pop())
            else:
                print('error')
        elif s == 'front':
            if len(deque_) > 0:
                print(deque_[0])
            else:
                print('error')
        elif s == 'back':
            if len(deque_) > 0:
                print(deque_[-1])
            else:
                print('error')
        elif s == 'size':
            print(len(deque_))
        elif s == 'clear':
            deque_.clear()
            print('ok')
        elif s.split()[0] == 'push_front':
            print('ok')
            deque_.appendleft(int(s.split()[1]))
        else:
            print('ok')
            deque_.append(int(s.split()[1]))
    print('bye')