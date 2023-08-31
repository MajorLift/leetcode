# Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Accepted 2023-08-31 22:57 UTC · Python · 231 ms · 35.7 MB

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.hasChild(char):
                curr.addChild(char)
            curr = curr.getChild(char)
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not curr.hasChild(char):
                return False
            curr = curr.getChild(char)
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not curr.hasChild(char):
                return False
            curr = curr.getChild(char)
        return True

    @staticmethod
    def getOrd(char):
        return ord(char) - ord('a')

class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = [None] * 26
        self.isEnd = False

    def __repr__(self):
        return f'val: {self.val}, children: {self.children}, isEnd: {self.isEnd}'

    def hasChild(self, char):
        return self.children[Trie.getOrd(char)] is not None
    
    def getChild(self, char):
        return self.children[Trie.getOrd(char)]

    def addChild(self, char):
        self.children[Trie.getOrd(char)] = TrieNode(char)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
