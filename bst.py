# Driver function
def __main__():
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    print(bst.search(30))
    bst.delete(30)
    print(bst.search(30))

# Data definition
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def __str__(self):
        return f"Node with value: {self.key}!"

# Data structure
class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    # Search a node
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # Delete a node
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    # Find the node with minimum value
    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

# Execution if executes directly
if __name__ == "__main__":
    __main__();