class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if not current_node.left_child:
                current_node.left_child = Node(data)
            else:
                self._insert_recursive(current_node.left_child, data)
        else:
            if not current_node.right_child:
                current_node.right_child = Node(data)
            else:
                self._insert_recursive(current_node.right_child, data)

    def search(self, data):
        return self._search_tree(self.root, data)

    def _search_tree(self, current_node, data):
        if not current_node:
            return False
        if current_node.data == data:
            return True
        elif data < current_node.data:
            return self._search_tree(current_node.left_child, data)
        else:
            return self._search_tree(current_node.right_child, data)


class RedBlackTree:
    RED = True
    BLACK = False

    class RedBlackNode:
        def __init__(self, data, color=True):
            self.data = data
            self.color = color
            self.left_child = None
            self.right_child = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        self.root.color = self.BLACK  # Root node must always be black

    def _insert(self, current_node, data):
        if current_node is None:
            return self.RedBlackNode(data)

        if data < current_node.data:
            current_node.left_child = self._insert(current_node.left_child, data)
        elif data > current_node.data:
            current_node.right_child = self._insert(current_node.right_child, data)

        if self._is_red_color(current_node.right_child) and not self._is_red_color(current_node.left_child):
            current_node = self._rotate_left(current_node)
        if self._is_red_color(current_node.left_child) and self._is_red_color(current_node.left_child.left_child):
            current_node = self._rotate_right(current_node)
        if self._is_red_color(current_node.left_child) and self._is_red_color(current_node.right_child):
            self._change_colors(current_node)

        return current_node

    def _is_red_color(self, current_node):
        return current_node is not None and current_node.color == self.RED

    def _rotate_left(self, current_node):
        temp = current_node.right_child
        current_node.right_child = temp.left_child
        temp.left_child = current_node
        temp.color = current_node.color
        current_node.color = self.RED
        return temp

    def _rotate_right(self, current_node):
        temp = current_node.left_child
        current_node.left_child = temp.right_child
        temp.right_child = current_node
        temp.color = current_node.color
        current_node.color = self.RED
        return temp

    def _change_colors(self, current_node):
        current_node.color = not current_node.color
        current_node.left_child.color = not current_node.left_child.color
        current_node.right_child.color = not current_node.right_child.color

    def search(self, data):
        return self._search_tree(self.root, data)

    def _search_tree(self, current_node, data):
        if not current_node:
            return False
        if current_node.data == data:
            return True
        elif data < current_node.data:
            return self._search_tree(current_node.left_child, data)
        else:
            return self._search_tree(current_node.right_child, data)


class AVLTree:
    class AVLNode:
        def __init__(self, data):
            self.data = data
            self.left_child = None
            self.right_child = None
            self.height = 1

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, current_node, data):
        if not current_node:
            return self.AVLNode(data)
        if data < current_node.data:
            current_node.left_child = self._insert(current_node.left_child, data)
        else:
            current_node.right_child = self._insert(current_node.right_child, data)

        current_node.height = 1 + max(self._get_height(current_node.left_child), self._get_height(current_node.right_child))

        balance = self._get_balance(current_node)

        # Left Left Case
        if balance > 1 and data < current_node.left_child.data:
            return self._rotate_right(current_node)

        # Right Right Case
        if balance < -1 and data > current_node.right_child.data:
            return self._rotate_left(current_node)

        # Left Right Case
        if balance > 1 and data > current_node.left_child.data:
            current_node.left_child = self._rotate_left(current_node.left_child)
            return self._rotate_right(current_node)

        # Right Left Case
        if balance < -1 and data < current_node.right_child.data:
            current_node.right_child = self._rotate_right(current_node.right_child)
            return self._rotate_left(current_node)

        return current_node

    def _get_height(self, current_node):
        if not current_node:
            return 0
        return current_node.height

    def _get_balance(self, current_node):
        if not current_node:
            return 0
        return self._get_height(current_node.left_child) - self._get_height(current_node.right_child)

    def _rotate_left(self, z):
        y = z.right_child
        T2 = y.left_child

        y.left_child = z
        z.right_child = T2

        z.height = 1 + max(self._get_height(z.left_child), self._get_height(z.right_child))
        y.height = 1 + max(self._get_height(y.left_child), self._get_height(y.right_child))

        return y

    def _rotate_right(self, y):
        x = y.left_child
        T2 = x.right_child

        x.right_child = y
        y.left_child = T2

        y.height = 1 + max(self._get_height(y.left_child), self._get_height(y.right_child))
        x.height = 1 + max(self._get_height(x.left_child), self._get_height(x.right_child))

        return x

    def search(self, data):
        return self._search_tree(self.root, data)

    def _search_tree(self, current_node, data):
        if not current_node:
            return False
        if current_node.data == data:
            return True
        elif data < current_node.data:
            return self._search_tree(current_node.left_child, data)
        else:
            return self._search_tree(current_node.right_child, data)


# Tests for Binary Search Tree
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Binary Search Tree:")
print(bst.search(5))  # Output: True
print(bst.search(10))  # Output: False

# Tests for Red-Black Tree
rbt = RedBlackTree()
rbt.insert(5)
rbt.insert(3)
rbt.insert(7)
rbt.insert(2)
rbt.insert(4)
rbt.insert(6)
rbt.insert(8)

print("\nRed-Black Tree:")
print(rbt.search(5))  # Output: True
print(rbt.search(10))  # Output: False

# Tests for AVL Tree
avl = AVLTree()
avl.insert(5)
avl.insert(3)
avl.insert(7)
avl.insert(2)
avl.insert(4)
avl.insert(6)
avl.insert(8)

print("\nAVL Tree:")
print(avl.search(5))  # Output: True
print(avl.search(10))  # Output: False
