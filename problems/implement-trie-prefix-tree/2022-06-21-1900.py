# Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Accepted 2022-06-21 19:00 UTC · Python · 477 ms · 31.5 MB

class TrieNode:
    
    def __init__(self, char = ""):
        self.char = char
        self.children = {}
        self.is_end = False

    def hasChild(self, char: str) -> bool:
        return char in self.children

    def addChild(self, char: str) -> None:
        self.children[char] = TrieNode(char)

    def getChild(self, char: str):
        if not self.hasChild(char):
            return
        return self.children[char]

    def isEnd(self) -> bool:
        return self.is_end

    def setEnd(self) -> None:
        self.is_end = True

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.hasChild(char):
                curr.addChild(char)
            curr = curr.getChild(char)
        curr.setEnd()

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if curr.hasChild(char):
                curr = curr.getChild(char)
            else:
                return False
        return curr.isEnd()

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        i = 0
        for char in prefix:
            if curr.hasChild(char):
                curr = curr.getChild(char)
                i += 1
            else:
                break
        return i == len(prefix)
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
