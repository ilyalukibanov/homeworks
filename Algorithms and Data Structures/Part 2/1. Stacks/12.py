stack = []
pairs = {']':'[', ')':'(','}':'{'}
parentheses = input()
is_correct = 'yes'
for parenthesis in parentheses:
    if parenthesis in pairs:
        if (len(stack) == 0) or (stack.pop() != pairs[parenthesis]):
            is_correct = 'no'
            break 
    else:
        stack.append(parenthesis)
if len(stack) > 0:
    is_correct = 'no'
print(is_correct)
