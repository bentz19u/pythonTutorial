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
