from entities.tree_node import TreeNode

# example to test the class
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

tree = TreeNode.parse_tuple(tree_tuple)

# it has to be rotated mentally to 90 degrees on the right
tree.display_keys()

# in order traversal
traversed_in_order_tree = tree.traverse_in_order()
print(traversed_in_order_tree)

# pre order traversal
traversed_pre_order_tree = tree.traverse_in_pre_order()
print(traversed_pre_order_tree)

# post order traversal
traversed_post_order_tree = tree.traverse_in_post_order()
print(traversed_post_order_tree)

# finding the height of a tree
# longest path of the tree from the root node to a leaf node
print(tree.get_tree_height())

# finding the size of a tree
# total number of nodes including the root and leaf nodes
print(tree.get_tree_size())

# A binary search tree or BST is a binary tree that satisfies the following conditions:
#     The left subtree of any node only contains nodes with keys less than the node's key
#     The right subtree of any node only contains nodes with keys greater than the node's key
is_bst = tree.is_bst()
print(is_bst)

# testing new tree of names
tree2 = TreeNode.parse_tuple((('caesar', 'daniel', 'eric')  , 'john', ('pluto', 'valerie', 'zachary')))
is_bst = tree2.is_bst()
print(is_bst)