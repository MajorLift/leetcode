# Word Search
# https://leetcode.com/problems/word-search/
# Accepted 2022-12-21 23:26 UTC · Python · 37 ms · 14 MB

from collections import Counter, defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)
        chars, valids = Counter(word), defaultdict(set)

        for i in range(m):
            for j in range(n):
                if board[i][j] in chars:
                    valids[board[i][j]].add((i, j))
        
        if len(chars) != len(valids) or not all([chars[k] <= len(valids[k]) for k in chars]):
            return False

        if len(valids[word[-1]]) < len(valids[word[0]]):
            word = word[::-1]
        
        def backtrack(curr, idx):
            if idx == k - 1:
                return True
            x, y = curr
            valids[word[idx]].remove((x, y))
            for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if (i, j) not in valids[word[idx + 1]]:
                    continue
                if backtrack((i, j), idx + 1):
                    return True
            valids[word[idx]].add((x, y))
            return False

        for i, j in [*valids[word[0]]]:
            if backtrack((i, j), 0):
                return True
        return False
