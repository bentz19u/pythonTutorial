from .bst_node import BSTNode


class TreeMap:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = self._find(self.root, key)
        if not node:
            self.root = self._insert(self.root, key, value)
            self.root = self.balance_bst()
        else:
            self._update(self.root, key, value)

    def __getitem__(self, key):
        node = self._find(self.root, key)
        return node.value if node else None

    # generator so it can be used in for loop
    def __iter__(self):
        return (x for x in self._list_all(self.root))

    def __len__(self):
        return TreeMap.get_tree_size(self.root)

    def display(self):
        return TreeMap.display_keys(self.root)

    def balance_bst(self):
        return self._make_balanced_bst(self._list_all(self.root))

    # Made BST from sorted array
    def _make_balanced_bst(self, data, low=0, high=None, parent=None):
        if high is None:
            high = len(data) - 1
        if low > high:
            return None

        mid = (low + high) // 2
        key, value = data[mid]

        node = BSTNode(key, value)
        node.parent = parent
        node.left = self._make_balanced_bst(data, low, mid - 1, node)
        node.right = self._make_balanced_bst(data, mid + 1, high, node)
        return node

    def _insert(self, node, key, value):
        # we reached a position where either left or right is empty
        if node is None:
            node = BSTNode(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
            node.left.parent = node
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
            node.right.parent = node
        return node

    def _find(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._find(node.left, key)
        if key > node.key:
            return self._find(node.right, key)

    def _update(self, node, key, value):
        target = self._find(node, key)
        if target is not None:
            target.value = value

    def _list_all(self, node):
        if node is None:
            return []
        return self._list_all(node.left) + [(node.key, node.value)] + self._list_all(node.right)

    @staticmethod
    def display_keys(node, space='\t', level=0):
        # If the node is empty
        if node is None:
            print(space * level + '∅')
            return

        # If the node is a leaf
        if node.left is None and node.right is None:
            print(space * level + str(node.key))
            return

        # If the node has children
        TreeMap.display_keys(node.right, space, level + 1)
        print(space * level + str(node.key))
        TreeMap.display_keys(node.left, space, level + 1)

    @staticmethod
    def get_tree_size(node):
        if node is None:
            return 0
        return 1 + TreeMap.get_tree_size(node.left) + TreeMap.get_tree_size(node.right)