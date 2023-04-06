def search(child, parent, path):
    if child in tree:
        path.append(tree[child])
        if tree[child] == parent:
            return 1, path
        else:
            return search(tree[child], parent, path)
    else:
        return 0, path

with open('input.txt', 'r') as file:
    tree = {}
    for i, row in enumerate(file):
        if i == 0:
            n = int(row)
        elif len(row) == 1: break
        else:
            name1, name2 = row.split()
            if i < n:
                tree[name1] = name2
            else:
                a, b = search(name1, name2, [name1])
                if a:
                    print(name2)
                else:
                    a, c = search(name2, name1, [name2])
                    if a:
                        print(name1)
                    else:
                        j = 0
                        if b == c:
                            print(b[0])
                        else:
                            while b[~j] == c[~j]:
                                j += 1
                            print(b[~(j-1)])
