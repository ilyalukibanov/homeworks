stack = []
while (s := input()) != 'exit':
    if s == 'pop':
        if len(stack) == 0:
            print('error')
        else:    
            print(stack.pop())
    elif s == 'back':
        if len(stack) == 0:
            print('error')
        else:    
            print(stack[-1])
    elif s == 'size':
        print(len(stack))
    elif s == 'clear':
        stack = []
        print('ok')
    else:
        stack.append(int(s.split()[-1]))
        print('ok')
print('bye')