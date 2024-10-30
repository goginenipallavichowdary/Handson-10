class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root_node = None

    def insert_node(self, value):
        if self.root_node is None:
            self.root_node = TreeNode(value)
        else:
            self._insert_node_recursive(self.root_node, value)

    def _insert_node_recursive(self, current, value):
        if value < current.value:
            if current.left_child is None:
                current.left_child = TreeNode(value)
            else:
                self._insert_node_recursive(current.left_child, value)
        else:
            if current.right_child is None:
                current.right_child = TreeNode(value)
            else:
                self._insert_node_recursive(current.right_child, value)

    def find_node(self, value):
        return self._find_node_recursive(self.root_node, value)

    def _find_node_recursive(self, current, value):
        if current is None or current.value == value:
            return current is not None
        elif value < current.value:
            return self._find_node_recursive(current.left_child, value)
        else:
            return self._find_node_recursive(current.right_child, value)

    def remove_node(self, value):
        self.root_node = self._remove_node_recursive(self.root_node, value)

    def _remove_node_recursive(self, current, value):
        if current is None:
            return current
        if value < current.value:
            current.left_child = self._remove_node_recursive(current.left_child, value)
        elif value > current.value:
            current.right_child = self._remove_node_recursive(current.right_child, value)
        else:
            if current.left_child is None:
                return current.right_child
            elif current.right_child is None:
                return current.left_child
            min_larger_node = self._find_min(current.right_child)
            current.value = min_larger_node.value
            current.right_child = self._remove_node_recursive(current.right_child, min_larger_node.value)
        return current

    def _find_min(self, current):
        while current.left_child is not None:
            current = current.left_child
        return current

    def inorder(self):
        result = []
        self._inorder_recursive(self.root_node, result)
        return result

    def _inorder_recursive(self, current, result):
        if current:
            self._inorder_recursive(current.left_child, result)
            result.append(current.value)
            self._inorder_recursive(current.right_child, result)

    def preorder(self):
        result = []
        self._preorder_recursive(self.root_node, result)
        return result

    def _preorder_recursive(self, current, result):
        if current:
            result.append(current.value)
            self._preorder_recursive(current.left_child, result)
            self._preorder_recursive(current.right_child, result)

    def postorder(self):
        result = []
        self._postorder_recursive(self.root_node, result)
        return result

    def _postorder_recursive(self, current, result):
        if current:
            self._postorder_recursive(current.left_child, result)
            self._postorder_recursive(current.right_child, result)
            result.append(current.value)

# Testing the modified Binary Tree implementation
bt = BinaryTree()

# Insert nodes with different values
for value in [60, 35, 25, 45, 85, 75, 95]:
    bt.insert_node(value)

# Traversals after insertion
inorder_result = bt.inorder()
preorder_result = bt.preorder()
postorder_result = bt.postorder()

# Search for nodes
search_60 = bt.find_node(60)  # Expected: True
search_40 = bt.find_node(40)  # Expected: False

# Delete a node
bt.remove_node(25)  # Delete leaf node
inorder_after_delete_leaf = bt.inorder()

bt.remove_node(35)  # Delete node with one child
inorder_after_delete_one_child = bt.inorder()

bt.remove_node(60)  # Delete node with two children
inorder_after_delete_two_children = bt.inorder()

# Output the test results
print("Inorder Traversal:", inorder_result)
print("Preorder Traversal:", preorder_result)
print("Postorder Traversal:", postorder_result)
print("Search for 60:", search_60)
print("Search for 40:", search_40)
print("Inorder after deleting 25:", inorder_after_delete_leaf)
print("Inorder after deleting 35:", inorder_after_delete_one_child)
print("Inorder after deleting 60:", inorder_after_delete_two_children)

# output:
# Inorder Traversal: [25, 35, 45, 60, 75, 85, 95]
# Preorder Traversal: [60, 35, 25, 45, 85, 75, 95]
# Postorder Traversal: [25, 45, 35, 75, 95, 85, 60]
# Search for 60: True
# Search for 40: False
# Inorder after deleting 25: [35, 45, 60, 75, 85, 95]
# Inorder after deleting 35: [45, 60, 75, 85, 95]
# Inorder after deleting 60: [45, 75, 85, 95]
