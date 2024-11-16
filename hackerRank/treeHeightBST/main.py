from jovian.pythondsa import evaluate_test_case

from dictionnaries.tests import test

# The height of a binary tree is the number of edges between the tree's root and its furthest leaf

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

1. generic case
3. empty tree
4. tree has only the root
"""

def height(root, current_height = 0):
    if root is None:
        # we remove 1 to the height because it was added when calling the function
        return current_height - 1

    left_tree_height = height(root['left'], current_height + 1)
    right_tree_height = height(root['right'], current_height + 1)

    return max(left_tree_height, right_tree_height)

result = evaluate_test_case(height, test)
print(result)