def search(child, parent, tree):
    if child in tree:
        if tree[child] == parent:
            return 1
        else:
            return search(tree[child], parent, tree)
    else:
        return 0

with open('input.txt', 'r') as file:
    tree = {}
    ans = []
    for i, row in enumerate(file):
        if i == 0:
            n = int(row)
        elif len(row) == 1: break
        else:
            name1, name2 = row.split()
            if i < n:
                tree[name1] = name2
            else:
                if search(name1, name2, tree):
                    ans.append(2)
                elif search(name2, name1, tree):
                    ans.append(1)
                else:
                    ans.append(0)
    print(*ans)
