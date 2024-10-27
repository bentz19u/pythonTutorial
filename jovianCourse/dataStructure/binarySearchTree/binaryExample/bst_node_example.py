from entities.user import User
from entities.bst_node import BSTNode

# samples of users
eric = User('eric', 'Eric Doe', 'eric@doe.com')
john = User('john', 'John Doe', 'john@doe.com')
pluto = User('pluto', 'Pluto Doe', 'pluto@doe.com')
valerie = User('valerie', 'Valerie Doe', 'juliette@doe.com')
zachary = User('zachary', 'Zachary Doe', 'zachary@doe.com')
caesar = User('caesar', 'Caesar Doe', 'caesar@doe.com')
daniel = User('daniel', 'Daniel Doe', 'daniel@doe.com')


# Level 0
# tree2 = TreeNode.parse_tuple((('caesar', 'daniel', 'eric')  , 'john', ('pluto', 'valerie', 'zachary')))

def insert(node, key, value):
    # we reached a position where either left or right is empty
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)


def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value


def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


unbalance_tree = insert(None, john.username, john)
insert(unbalance_tree, eric.username, eric)
insert(unbalance_tree, pluto.username, pluto)
insert(unbalance_tree, valerie.username, valerie)
insert(unbalance_tree, zachary.username, zachary)
insert(unbalance_tree, caesar.username, caesar)
insert(unbalance_tree, daniel.username, daniel)

unbalance_tree.display_keys()

node = find(unbalance_tree, zachary.username)
print(node.key, node.value)

update(unbalance_tree, zachary.username, User(zachary.username, 'Testing', 'testing@example.com'))

node = find(unbalance_tree, zachary.username)
print(node.key, node.value)

list_tree = list_all(unbalance_tree)
print(list_tree)

is_balanced = unbalance_tree.is_balanced()
print(is_balanced)

# O(N) complexity because the tree is unbalanced and can change greatly depending on the order or insertion

users = [caesar, daniel, eric, john, pluto, valerie, zachary]
data = [(user.username, user) for user in users]
balanced_tree = BSTNode.make_balanced_bst(data)
print(balanced_tree)

is_balanced = balanced_tree.is_balanced()
print(is_balanced)

balanced_tree.display_keys()


# we can now balance the unbalanced tree by just making a new BST from the sorted array
def balance_bst(tree):
    return BSTNode.make_balanced_bst(list_all(tree))


tree = balance_bst(unbalance_tree)
is_balanced = tree.is_balanced()
print(is_balanced)
