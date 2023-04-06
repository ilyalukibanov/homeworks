class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

    def add(self, value):
        if self.val:
            if self.val == value:
                return 'ALREADY'
            elif self.val > value:
                if self.left == None:
                    self.left = Tree(value)
                    return 'DONE'
                else:
                    return self.left.add(value)
            else:
                if self.right == None:
                    self.right = Tree(value)
                    return 'DONE'
                else:
                    return self.right.add(value)
        else:
            self.val = value
            return 'DONE'

    def search(self, value):
        if self.val:
            if self.val == value:
                return 'YES'
            elif self.val > value:
                if self.left:
                    return self.left.search(value)
                else:
                    return "NO"
            else:
                if self.right:
                    return self.right.search(value)
                else:
                    return 'NO'
        else:
            return 'NO'

    def print_tree(self, depth):
        if self.left:
            self.left.print_tree(depth+1)
        print('.'*depth, end='')
        print(self.val)
        if self.right:
            self.right.print_tree(depth+1)


with open('input.txt', 'r') as file:
    tree = Tree(None)
    for row in file:
        if len(row) == 1: break
        else:
            if row == 'PRINTTREE\n':
                tree.print_tree(0)
            else:
                action, number = row.split()
                number = int(number)
                if action == 'ADD':
                    print(tree.add(number))
                else:
                    print(tree.search(number))
