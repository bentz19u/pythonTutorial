from jovian.pythondsa import evaluate_test_case

from dictionnaries.tests import test, tests

# Is it a BST?
# For example, the image on the left below is a valid BST.
# The data value of every node in a node's left subtree is less than the data value of that node.
# The data value of every node in a node's right subtree is greater than the data value of that node.
# The data value of every node is distinct.

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''

"""
Possible cases

1. is BST
2. is not BST because values is misplaced
3. duplication of node info
"""

# version for hackerrank
# def checkBST(root):
#     memo = []
#
#     def recursive(root,
#                   parent_data = None,
#                   is_left = False,
#                   is_right = False):
#         if root is None:
#             return True
#
#         value = root.data
#         if value in memo:
#             return False
#
#         memo.append(value)
#
#         if root.left is not None:
#             if root.left.data > root.data:
#                 return False
#             if is_right and root.left.data < parent_data:
#                 return False
#         if root.right is not None:
#             if root.right.data < root.data:
#                 return False
#             if is_left and root.right.data > parent_data:
#                 return False
#
#         left_tree_is_binary = recursive(root.left, root.data, True, False)
#         right_tree_is_binary = recursive(root.right, root.data, False, True)
#
#         return left_tree_is_binary and right_tree_is_binary
#
#     return recursive(root)

def checkBST_old(root):
    # we keep in memory the info found at each node
    memo = []

    def recursive(root, parent_info = None, is_left = False, is_right = False):
        if root is None:
            return True

        # we found a duplicate, according to the rule, it's not a valid BST
        value = root['info']
        if value in memo:
            return False

        memo.append(value)

        if root['left'] is not None:
            if root['left']['info'] > root['info']:
                return False
            # in right tree, only the left node can be potentially lower than the parent node
            if is_right and root['left']['info'] < parent_info:
                return False
        if root['right'] is not None:
            if root['right']['info'] < root['info']:
                return False
            # in left tree, only the right node can be potentially higher than the parent node
            if is_left and root['right']['info'] > parent_info:
                return False

        left_tree_is_binary = recursive(root['left'], root['info'], True, False)
        right_tree_is_binary = recursive(root['right'], root['info'], False, True)

        return left_tree_is_binary and right_tree_is_binary

    return recursive(root)

# old version didn't work because of case `long_tree_no_bst` in the imgs file
# now, we will check that the tree is `in order traversal`
def checkBST(root):
    def in_order_traversal(node, previous = None):
        if node is None:
            return True, previous

        # Then check left node
        if node['left'] is not None:
            left_tree_is_binary, _ = in_order_traversal(node['left'], previous)
            if left_tree_is_binary is False:
                return False, previous

        # Check the current node
        if previous is not None and previous >= node['info']:
            return False, previous

        # Update the previous value
        previous = node['info']

        # Then check right node
        if node['right'] is not None:
            right_tree_is_binary, _ = in_order_traversal(node['right'], previous)
            if right_tree_is_binary is False:
                return False, previous

        return True, previous

    is_valid_bst, _ = in_order_traversal(root)
    return is_valid_bst

# result = evaluate_test_case(checkBST, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(checkBST, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
