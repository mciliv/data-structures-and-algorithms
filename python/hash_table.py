# TODO: Implement chaining


# Hash table for characters
class HashTable:
    def __init__(self):
        self.table = 26 * [None]

    def hash(self, x):
        return ord(x) - ord("a")

    def get(self, key):
        """gets the value from the table given the key and returns it"""
        return self.table[self.hash(key)]

    def set(self, key, value):
        """sets the value in the table, and returns the table"""
        self.table[self.hash(key)] = value
        return value
