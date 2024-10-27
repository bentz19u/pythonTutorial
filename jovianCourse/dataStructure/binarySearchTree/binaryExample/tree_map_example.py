from entities.tree_map import TreeMap
from entities.user import User

# samples of users
eric = User('eric', 'Eric Doe', 'eric@doe.com')
john = User('john', 'John Doe', 'john@doe.com')
pluto = User('pluto', 'Pluto Doe', 'pluto@doe.com')
valerie = User('valerie', 'Valerie Doe', 'juliette@doe.com')
zachary = User('zachary', 'Zachary Doe', 'zachary@doe.com')
caesar = User('caesar', 'Caesar Doe', 'caesar@doe.com')
daniel = User('daniel', 'Daniel Doe', 'daniel@doe.com')

# testing TreeMap class that has all the methods above
print('testing TreeMap')
treemap = TreeMap()
treemap.display()

# this used __setitem__ to insert the new element
treemap['eric'] = eric
treemap['john'] = john
treemap['pluto'] = pluto

treemap.display()

# we can now get the BSTNode like this
pluto_from_tree = treemap['pluto']
print(pluto_from_tree)

length_tree = len(treemap)
print(length_tree)

treemap['valerie'] = valerie
treemap['zachary'] = zachary
treemap['caesar'] = caesar
treemap['daniel'] = daniel

length_tree = len(treemap)
print(length_tree)

treemap.display()

# we can print the sorted array thanks to __iter__
list = list(treemap)
print(list)