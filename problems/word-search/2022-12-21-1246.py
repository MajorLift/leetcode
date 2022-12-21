# Word Search
# https://leetcode.com/problems/word-search/
# Accepted 2022-12-21 12:46 UTC · Python · 4059 ms · 13.9 MB

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)
        if m * n < k or not set([e for row in board for e in row]).issuperset(set([*word])):
            return False

        visited = set()
        def backtrack(curr, idx):
            x, y = curr
            if not (0 <= x < m and 0 <= y < n) or board[x][y] != word[idx] or (x, y) in visited:
                return False
            if idx == k - 1:
                return True

            res = False
            visited.add(curr)
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                res = backtrack((i, j), idx + 1)
                if res:
                    break
            visited.remove(curr)
            return res

        starts = [(i, j) for i in range(m) for j in range(n) if board[i][j] == word[0]]
        for i, j in starts:
            if backtrack((i, j), 0):
                return True
        return False
