from entities.user import User
from databases.user_database import UserDatabase

# We need to create a data structure which can store 100 million records and perform insertion, search, update and list operations efficiently.

# samples of users
eric = User('eric', 'Eric Doe', 'eric@doe.com')
john = User('john', 'John Doe', 'john@doe.com')
pluto = User('pluto', 'Pluto Doe', 'pluto@doe.com')
valerie = User('valerie', 'Valerie Doe', 'juliette@doe.com')
zachary = User('zachary', 'Zachary Doe', 'zachary@doe.com')
caesar = User('caesar', 'Caesar Doe', 'caesar@doe.com')
daniel = User('daniel', 'Daniel Doe', 'daniel@doe.com')

users = [caesar, daniel, eric, john, pluto, valerie, zachary]

database = UserDatabase()

for user in users:
    database.insert(user)

print(database.find('valerie'))

user = database.find('valerie')

user.email = 'toto'
database.update(user)
database.update(User(username='zachary', name='zachary U', email='zachary@doe.com'))

print(database.find('valerie'))
print(database.find('zachary'))

chris = User('chris', 'Chris Doe', 'chris@doe.com')

database.insert(chris)
users = database.list_all()
print(users)

# super slow
# Insert: O(N)
# Find: O(N)
# Update: O(N)
# List: O(1)
