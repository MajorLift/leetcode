# Design Search Autocomplete System
# https://leetcode.com/problems/design-search-autocomplete-system/
# Accepted 2023-04-30 20:08 UTC · Python · 621 ms · 22.2 MB

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.n = len(sentences)
        self.root = TrieNode()
        self.stream = ""
        for sentence, freq in zip(sentences, times):
            self.add(sentence, freq)

    def add(self, sentence, hot):
        curr = self.root
        for char in sentence:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True
        curr.val = sentence
        curr.rank -= hot

    def search(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        pq, stack = [], [curr]
        while stack:
            curr = stack.pop()
            if curr.isEnd:
                heappush(pq, (curr.rank, curr.val))
            for child in curr.children:
                stack.append(curr.children[child])
        return pq

    def input(self, c: str) -> List[str]:
        results = []
        if c == "#":
            self.add(self.stream, 1)
            self.stream = ""
        else:
            self.stream += c
            results = self.search(self.stream)
        
        output = []
        for _ in range(3):
            if not results:
                break
            _, sentence = heappop(results)
            output.append(sentence)
        return output


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.val = None
        self.rank = 0

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
