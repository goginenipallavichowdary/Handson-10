class NodeAVL:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left_child = None
        self.right_child = None

class TreeAVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts a value into the AVL Tree."""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return NodeAVL(value)
        if value < node.value:
            node.left_child = self._insert_recursive(node.left_child, value)
        elif value > node.value:
            node.right_child = self._insert_recursive(node.right_child, value)
        else:
            return node  # No duplicates allowed

        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))
        balance = self._get_balance(node)

        # Left heavy
        if balance > 1 and value < node.left_child.value:
            return self._rotate_right(node)
        # Right heavy
        if balance < -1 and value > node.right_child.value:
            return self._rotate_left(node)
        # Left-Right case
        if balance > 1 and value > node.left_child.value:
            node.left_child = self._rotate_left(node.left_child)
            return self._rotate_right(node)
        # Right-Left case
        if balance < -1 and value < node.right_child.value:
            node.right_child = self._rotate_right(node.right_child)
            return self._rotate_left(node)

        return node

    def delete(self, value):
        """Deletes a value from the AVL Tree."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left_child = self._delete_recursive(node.left_child, value)
        elif value > node.value:
            node.right_child = self._delete_recursive(node.right_child, value)
        else:
            if not node.left_child:
                return node.right_child
            elif not node.right_child:
                return node.left_child
            temp = self._get_min_value_node(node.right_child)
            node.value = temp.value
            node.right_child = self._delete_recursive(node.right_child, temp.value)

        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))
        balance = self._get_balance(node)

        # Balance the node if needed
        if balance > 1 and self._get_balance(node.left_child) >= 0:
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right_child) <= 0:
            return self._rotate_left(node)
        if balance > 1 and self._get_balance(node.left_child) < 0:
            node.left_child = self._rotate_left(node.left_child)
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right_child) > 0:
            node.right_child = self._rotate_right(node.right_child)
            return self._rotate_left(node)

        return node

    def search(self, value):
        """Searches for a value in the AVL Tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node or node.value == value:
            return node is not None
        if value < node.value:
            return self._search_recursive(node.left_child, value)
        return self._search_recursive(node.right_child, value)

    def inorder_traversal(self):
        """Returns a list of nodes in in-order traversal."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left_child, result)
            result.append(node.value)
            self._inorder_recursive(node.right_child, result)

    def _rotate_left(self, z):
        y = z.right_child
        T2 = y.left_child
        y.left_child = z
        z.right_child = T2
        z.height = 1 + max(self._get_height(z.left_child), self._get_height(z.right_child))
        y.height = 1 + max(self._get_height(y.left_child), self._get_height(y.right_child))
        return y

    def _rotate_right(self, z):
        y = z.left_child
        T3 = y.right_child
        y.right_child = z
        z.left_child = T3
        z.height = 1 + max(self._get_height(z.left_child), self._get_height(z.right_child))
        y.height = 1 + max(self._get_height(y.left_child), self._get_height(y.right_child))
        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left_child) - self._get_height(node.right_child)

    def _get_min_value_node(self, node):
        while node.left_child:
            node = node.left_child
        return node


# Testing the modified AVL Tree Implementation
avl_tree = TreeAVL()

# Insert nodes with different values
for value in [40, 25, 50, 15, 35, 5, 30, 60, 70]:
    avl_tree.insert(value)

# In-order traversal before deletion
inorder_before_delete = avl_tree.inorder_traversal()

# Searching for nodes
search_30 = avl_tree.search(30)  # Expected: True
search_100 = avl_tree.search(100)  # Expected: False

# Deleting nodes
avl_tree.delete(5)   # Deleting a leaf node
inorder_after_delete_5 = avl_tree.inorder_traversal()

avl_tree.delete(15)  # Deleting node with one child
inorder_after_delete_15 = avl_tree.inorder_traversal()

avl_tree.delete(40)  # Deleting node with two children
inorder_after_delete_40 = avl_tree.inorder_traversal()

# Output the test results
print("Inorder Traversal Before Deletion:", inorder_before_delete)
print("Search for 30:", search_30)
print("Search for 100:", search_100)
print("Inorder Traversal After Deleting 5:", inorder_after_delete_5)
print("Inorder Traversal After Deleting 15:", inorder_after_delete_15)
print("Inorder Traversal After Deleting 40:", inorder_after_delete_40)

# Expected Output:
# Inorder Traversal Before Deletion: [5, 15, 25, 30, 35, 40, 50, 60, 70]
# Search for 30: True
# Search for 100: False
# Inorder Traversal After Deleting 5: [15, 25, 30, 35, 40, 50, 60, 70]
# Inorder Traversal After Deleting 15: [25, 30, 35, 40, 50, 60, 70]
# Inorder Traversal After Deleting 40: [25, 30, 35, 50, 60, 70]

