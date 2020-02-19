# Implement a trie with insert, search, and startsWith methods.
#
# Note:
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for letter in word:
            node = node.setdefault(letter, {})
        node['*'] = None

    def _search(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return {}
            node = node[letter]
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return '*' in self._search(word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return bool(self._search(prefix))




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
