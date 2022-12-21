# Word Search
# https://leetcode.com/problems/word-search/
# Accepted 2022-12-21 12:50 UTC · Python · 3446 ms · 14.1 MB

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)

        board_chars, word_chars = set([e for row in board for e in row]), set([*word])
        if m * n < k or not board_chars.issuperset(word_chars):
            return False

        visited = set()
        def backtrack(curr, idx):
            x, y = curr
            if not (0 <= x < m and 0 <= y < n) or board[x][y] != word[idx] or (x, y) in visited:
                return False
            if idx == k - 1:
                return True

            visited.add(curr)
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if backtrack((i, j), idx + 1):
                    return True
            visited.remove(curr)
            return False

        return any([backtrack((i, j), 0) for i, j in [(i, j) for i in range(m) for j in range(n) if board[i][j] == word[0]]])
