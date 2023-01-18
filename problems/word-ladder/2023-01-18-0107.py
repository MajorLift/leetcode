# Word Ladder
# https://leetcode.com/problems/word-ladder/
# Accepted 2023-01-18 01:07 UTC · Python · 666 ms · 15.1 MB

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words, visited = set(wordList), set()
        queue = deque([beginWord])
        dist = 0
        while queue:
            dist += 1
            next_queue = deque([])
            while queue:
                word = queue.popleft()
                if word == endWord:
                    return dist
                for i in range(len(word)):
                    for k in range(26):
                        s = word[:i] + chr(ord("a") + k) + word[i+1:]
                        if s not in visited and s in words:
                            visited.add(s)
                            next_queue.append(s)
            queue = next_queue
        return 0
