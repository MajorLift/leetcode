# Word Ladder
# https://leetcode.com/problems/word-ladder/
# Accepted 2022-10-23 01:19 UTC · Python · 907 ms · 15.1 MB

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words, visited = set(wordList), set()
        queue = deque([beginWord])
        changes = 1
        while queue:
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                if curr == endWord:
                    return changes
                for i in range(len(curr)):
                    for k in range(26):
                        s = curr[:i] + chr(ord('a') + k) + curr[i+1:]
                        if s in words and s not in visited:
                            queue.append(s)
                            visited.add(s)
            changes += 1
        return 0
