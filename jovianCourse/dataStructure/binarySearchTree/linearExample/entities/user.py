class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    # in python, the __repr__() method is a special method used to define a string representation of an object.
    # mostly for devs, is return when using print()
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    # same as __repr__ but to show to the user
    def __str__(self):
        return self.__repr__()