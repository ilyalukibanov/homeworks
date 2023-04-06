from collections import deque
with open('input.txt', 'r') as file:
    hand1 = deque()
    hand1.extend((list(map(int, file.readline().split()))))
    hand2 = deque()
    hand2.extend(list(map(int, file.readline().split())))
    count = 0
    MAX_COUNT = 1_000_000
    while hand1 and hand2 and (count < MAX_COUNT):
        first = hand1.popleft()
        second = hand2.popleft()
        if ((first > second) and not (first == 9 and second == 0)) or (first == 0 and second == 9):
            hand1.extend([first, second])
        else:
            hand2.extend([first, second])
        count += 1
    if count == MAX_COUNT:
        print('botva')
    elif hand1:
        print(f'first {count}')
    else:
        print(f'second {count}')