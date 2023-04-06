stack = []
to_compute = list(input().split())
for value in to_compute:
    if value == '+':
        stack.append(stack.pop()+stack.pop())
    elif value == '-':
        stack.append(-stack.pop()+stack.pop())
    elif value == '*':
        stack.append(stack.pop()*stack.pop())
    else:
        stack.append(int(value))
print(stack.pop())