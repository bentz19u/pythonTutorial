# List [] = mutable, most flexible
# Tuple () = immutable, faster
# Set {}  = mutable (add/remove) unordered, NO duplicates, best for membership testing

fruits = ["apple", "pear", "orange", "coconut"]

fruits.append("mango")
fruits.remove("pear")
fruits.pop(1)  # remove at index
# fruits.clear()  # remove the whole list

for fruit in fruits:
    print(fruit, end=' ')

tupleFruits = ("apple", "pear", "orange", "coconut")

# cannot be changed
# tupleFruits.append("mango")
# tupleFruits.remove("pear")
# tupleFruits.pop(1)  # remove at index
# tupleFruits.clear()  # remove the whole list

print("\n")

setFruits = {"apple", "pear", "orange", "coconut"}

setFruits.add("mango")
setFruits.remove("apple")
# doest work
# setFruits[0] = "pineapple"

# order change everytime it's run
for fruit in setFruits:
    print(fruit, end=' ')

# checking membership of the set
print("\n")

if "apple" in setFruits:
    print("apple was found")
else:
    print('apple was not found')



