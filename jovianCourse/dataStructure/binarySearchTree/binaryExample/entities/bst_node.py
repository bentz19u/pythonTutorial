class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space * level + '∅')
            return

        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # If the node has children
        BSTNode.display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        BSTNode.display_keys(self.left, space, level + 1)

    def is_balanced(self):
        # Ensure that the left subtree is balanced.
        # Ensure that the right subtree is balanced.
        # Ensure that the difference between heights of left subtree and right subtree is not more than 1.

        if self is None:
            return True, 0

        balance_left, height_left = BSTNode.is_balanced(self.left)
        balance_right, height_right = BSTNode.is_balanced(self.right)
        balanced = balance_left and balance_right and abs(height_left - height_right) <= 1
        height = 1 + max(height_left, height_right)
        return balanced, height

    # Made BST from sorted array
    @staticmethod
    def make_balanced_bst(data, low=0, high=None, parent=None):
        if high is None:
            high = len(data) - 1
        if low > high:
            return None

        mid = (low + high) // 2
        key, value = data[mid]

        node = BSTNode(key, value)
        node.parent = parent
        node.left = BSTNode.make_balanced_bst(data, low, mid - 1, node)
        node.right = BSTNode.make_balanced_bst(data, mid + 1, high, node)
        return node
