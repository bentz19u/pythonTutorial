class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def get_tree_height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.get_tree_height(self.left), TreeNode.get_tree_height(self.right))

    def get_tree_size(self):
        if self is None:
            return 0
        return 1 + TreeNode.get_tree_size(self.left) + TreeNode.get_tree_size(self.right)

    # left -> root -> right
    def traverse_in_order(self):
        if self is None:
            return []
        return TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right)

    # root -> left -> right
    def traverse_in_pre_order(self):
        if self is None:
            return []
        return [self.key] + TreeNode.traverse_in_pre_order(self.left) + TreeNode.traverse_in_pre_order(self.right)

    # left -> right -> root
    def traverse_in_post_order(self):
        if self is None:
            return []
        return TreeNode.traverse_in_post_order(self.left) + TreeNode.traverse_in_post_order(self.right) + [self.key]

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
        TreeNode.display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        TreeNode.display_keys(self.left, space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node