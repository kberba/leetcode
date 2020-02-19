# Design a HashSet without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
# add(value): Insert a value into the HashSet.
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def add(self, key: int) -> None:
        # if the key doesn't exist, add it
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        # if key exists, delete it
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.data:
            return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
