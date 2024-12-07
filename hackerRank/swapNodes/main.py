from collections import deque


# Swapping subtrees of a node means that if initially node has left subtree L and right subtree R,
# then after swapping, the left subtree will be R and the right subtree, L.

# indexes = [[2, 3], [-1, -1], [-1, -1]]
# queries = [1,1]

def swapNodesExample(indexes, queries):
    return [[3, 1, 2], [2, 1, 3]]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def createNodeFromIndexes(indexes):
    root = Node(1)
    q = deque([root])

    for left_val, right_val in indexes:
        node = q.popleft()

        if left_val != -1:
            node.left = Node(left_val)
            q.append(node.left)
        if right_val != -1:
            node.right = Node(right_val)
            q.append(node.right)

    return root


def inOrder(root):
    values = []

    def inOrderTraversal(root):
        if root is None:
            return
        inOrderTraversal(root.left)
        values.append(root.value)
        inOrderTraversal(root.right)

    inOrderTraversal(root)
    return values


def swapNodes(indexes, queries):
    tree = createNodeFromIndexes(indexes)
    def recursive(tree, queries, result):
        q = deque([tree])
        pending_q = []
        current_height = 1
        while len(q) > 0:
            node = q.popleft()
            if current_height in queries:
                node.left, node.right = node.right, node.left
                print(f"current_height {current_height}")
                print(f"value {node.value}")
                print(inOrder(tree))

            if node.left is not None:
                pending_q.append(node.left)
            if node.right is not None:
                pending_q.append(node.right)

            if len(q) == 0 and len(pending_q) > 0:
                q += pending_q
                pending_q = []
                current_height += 1

        result.append(inOrder(tree))
        del(queries[0])
        if len(queries) > 0:
            result = recursive(tree, queries, result)

        return result

    return recursive(tree, queries, [])


# result = swapNodes([[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]], [2, 4])
result = swapNodes([[2,3],[4,5],[6,-1],[-1,7],[8,9],[10,11],[12,13],[-1,14],[-1,-1],[15,-1],[16,17],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]], [2, 3])
print(result)