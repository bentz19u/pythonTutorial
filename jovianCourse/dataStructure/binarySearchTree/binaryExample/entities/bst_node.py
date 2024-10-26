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