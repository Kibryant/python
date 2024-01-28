class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)
        else:
            print("Value already in tree!")

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(value, self.root)

    def _search(self, value, node):
        if value == node.value:
            return True
        elif value < node.value and node.left is not None:
            return self._search(value, node.left)
        elif value > node.value and node.right is not None:
            return self._search(value, node.right)
        return False

    def delete(self, value):
        if self.root is None:
            print("Tree is empty!")
        else:
            self._delete(value, self.root)

    def _delete(self, value, node):
        if value < node.value and node.left is not None:
            node.left = self._delete(value, node.left)
        elif value > node.value and node.right is not None:
            node.right = self._delete(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.value = self._find_min(node.right)
                node.right = self._delete(node.value, node.right)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def print_tree(self):
        if self.root is None:
            print("Tree is empty!")
        else:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.value) + " ", end="")
            self._print_tree(node.right)

    def print_tree_bfs(self):
        if self.root is None:
            print("Tree is empty!")
        else:
            self._print_tree_bfs(self.root)

    def _print_tree_bfs(self, node):
        queue = []
        queue.append(node)
        while len(queue) > 0:
            print(queue[0].value, end=" ")
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()


if __name__ == "__main__":
    tree = BinaryTree(None)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    print(tree.search(6))
    print(tree.search(10))
    tree.delete(5)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(7)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(3)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(1)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(4)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(6)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(8)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(10)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(5)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(3)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(7)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(1)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(4)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(6)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print()
    tree.delete(8)
    tree.print_tree()
    print()
    tree.print_tree_bfs()
    print
