def reconstruct_tree(s):
    tree = {'left': None, 'right': None, 'parent': None, 'type': 'root'}
    current_node = tree
    for char in s:
        if char == 'D':
            new_node = {'left': None, 'right': None, 'parent': current_node, 'type': 'left'}
            current_node['left'] = new_node
            current_node = new_node
        else:
            while current_node['type'] == 'right':
                current_node = current_node['parent']
            current_node = current_node['parent']
            new_node = {'left': None, 'right': None, 'parent': current_node, 'type': 'right'}
            current_node['right'] = new_node
            current_node = new_node
    return tree


def traverse_tree(root, prefix):
    if root['left'] is None and root['right'] is None:
        return [''.join(prefix)]
    prefix.append('0')
    ans = traverse_tree(root['left'], prefix)
    prefix.pop()
    prefix.append('1')

    ans.extend(traverse_tree(root['right'], prefix))
    prefix.pop()
    return ans


n = int(input())
answer = []
for i in range(n):
    s = input()
    tree = reconstruct_tree(s)
    prefixes = traverse_tree(tree, [])
    answer.append(str(len(prefixes)))
    answer.extend(prefixes)
print(answer)

for element in answer:
    for symbol in element:
        print(symbol, end='')
    print()

