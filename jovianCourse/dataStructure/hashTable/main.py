# example of Python dictionary
from entities.basic_hash_table import BasicHashTable
from entities.probing_hash_table import ProbingHashTable

phone_numbers = {
    'Daniel': '01085854444',
    'John': '01085855555',
    'Eric': '01085856666'
}

# print(phone_numbers)

# Add a new value
phone_numbers['Toto'] = '8787878787'
# Update existing value
phone_numbers['John'] = '7878787878'
# Accessing the value
# print(phone_numbers['John'])
# View the updated dictionary
# print(phone_numbers)

# now let's make our hashtable
basic_table = BasicHashTable(max_size=1024)

basic_table.insert('Daniel', '01085854444')
basic_table.insert('John', '01085855555')
basic_table.insert('Eric', '01085856666')

daniel = basic_table.find('Daniel')
print(daniel)

all_keys = basic_table.list_all()
print(all_keys)

# using probing hash table
# Create a new hash table
probing_table = ProbingHashTable()

# Insert a value
probing_table.insert('listen', 99)

# Check the value
result = probing_table.find('listen') == 99
print(result)

# Insert a colliding key
probing_table.insert('silent', 200)

# Check the new and old keys
print(probing_table.find('listen') == 99 and probing_table.find('silent') == 200)

# Update a key
probing_table.insert('listen', 101)

# Check the value
result = probing_table.find('listen') == 101
print(result)

result = probing_table.list_all() == ['listen', 'silent']
print(result)