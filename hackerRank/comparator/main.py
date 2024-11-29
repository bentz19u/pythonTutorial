from functools import cmp_to_key

# The Player class is provided in the editor below. It has two fields:
# name: a string
# score: an integer

# Given an array of n Player objects, write a comparator that sorts them in order of decreasing score.
# If 2 or more players have the same score, sort those players alphabetically ascending by name
# To do this, you must create a Checker class that implements the Comparator interface,
# then write an int compare(Player a, Player b) method implementing the

# Declare a Checker class that implements the comparator method as described.
# It should sort first descending by score, then ascending by name.
# The code stub reads the input, creates a list of Player objects, uses your method to sort the data, and prints it out properly.

# Example
# n = 3
# data = [[Smith, 20], [Jones, 15], [Jones, 20]]
# sorted = [[Jones, 20], [Smith, 20], [Jones, 15]]

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.score}"

    @staticmethod
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return +1
        else:
            return -1 if a.name < b.name else 1

players = [
    Player("Alice", 50),
    Player("Bob", 75),
    Player("Charlie", 75),
    Player("Daisy", 60)
]

sorted_players = sorted(players, key=cmp_to_key(Player.comparator))

for player in sorted_players:
    print(player)