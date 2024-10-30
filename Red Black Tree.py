class TreeNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left_child = None
        self.right_child = None
        self.node_color = "red"

    def __str__(self):
        return f"Key: {self.key}, Color: {self.node_color}, [Left: {self.left_child.key if self.left_child else None} | Right: {self.right_child.key if self.right_child else None}]"

class RedBlackTree:
    def __init__(self):
        self.root_node = None

    def is_empty(self):
        return self.root_node is None

    def insert(self, key, data):
        if self.is_empty():
            self.root_node = TreeNode(key, data)
            self.root_node.node_color = "black"
        else:
            self.root_node = self._insert(self.root_node, key, data)
            self.root_node.node_color = "black"

    def _insert(self, node, key, data):
        if node is None:
            return TreeNode(key, data)
        if key < node.key:
            node.left_child = self._insert(node.left_child, key, data)
        elif key > node.key:
            node.right_child = self._insert(node.right_child, key, data)
        else:
            node.data = data
        return self._balance(node)

    def remove(self, key):
        self.root_node = self._remove(self.root_node, key)

    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left_child = self._remove(node.left_child, key)
        elif key > node.key:
            node.right_child = self._remove(node.right_child, key)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            else:
                node.key = self._find_min(node.right_child).key
                node.data = self._find_min(node.right_child).data
                node.right_child = self._remove(node.right_child, node.key)
        return self._balance(node)

    def _balance(self, node):
        if node.node_color == "red" and node.left_child and node.left_child.node_color == "red":
            if node.right_child and node.right_child.node_color == "red":
                node.node_color = "red"
                node.left_child.node_color = "black"
                node.right_child.node_color = "black"
        return node

    def search(self, key):
        return self._search(self.root_node, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left_child, key)
        else:
            return self._search(node.right_child, key)

    def _find_min(self, node):
        while node.left_child:
            node = node.left_child
        return node

    def __str__(self):
        return "======== {Red-Black Tree} ==========\n" + self._print_tree(self.root_node) + "========================="

    def _print_tree(self, node):
        if node is None:
            return ""
        return self._print_tree(node.left_child) + str(node) + "\n" + self._print_tree(node.right_child)

if __name__ == '__main__':
    rbt = RedBlackTree()
    rbt.insert(15, "Fifteen")
    rbt.insert(25, "Twenty-Five")
    rbt.insert(35, "Thirty-Five")
    rbt.insert(45, "Forty-Five")
    print(rbt)
    print("{Root Node}: ", rbt.root_node)
    print("{Root Left Child}: ", rbt.root_node.left_child)
    print("{Root Right Child}: ", rbt.root_node.right_child)
    print("Removing 25 and 35...")
    rbt.remove(25)
    rbt.remove(35)
    print("{Root Left Child}: ", rbt.root_node.left_child)
    print("{Root Right Child}: ", rbt.root_node.right_child)
    print("{Search 15}: ", rbt.search(15))
    print("{Search 45}: ", rbt.search(45))
    print("{Search 35}: ", rbt.search(35))
    print(rbt)


# output
======== {Red-Black Tree} ==========
Key: 15, Color: black, [Left: None | Right: 25]
Key: 25, Color: red, [Left: None | Right: 35]
Key: 35, Color: red, [Left: None | Right: 45]
Key: 45, Color: red, [Left: None | Right: None]
=========================
{Root Node}:  Key: 15, Color: black, [Left: None | Right: 25]
{Root Left Child}:  None
{Root Right Child}:  Key: 25, Color: red, [Left: None | Right: 35]
Removing 25 and 35...
{Root Left Child}:  None
{Root Right Child}:  Key: 45, Color: red, [Left: None | Right: None]
{Search 15}:  Key: 15, Color: black, [Left: None | Right: 45]
{Search 45}:  Key: 45, Color: red, [Left: None | Right: None]
{Search 35}:  None
======== {Red-Black Tree} ==========
Key: 15, Color: black, [Left: None | Right: 45]
Key: 45, Color: red, [Left: None | Right: None]
=========================
