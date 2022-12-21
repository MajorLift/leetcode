# Word Search
# https://leetcode.com/problems/word-search/
# Accepted 2022-12-21 12:58 UTC · Python · 2578 ms · 14 MB

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)

        word_chars, board_chars = set([*word]), set([e for row in board for e in row])
        if m * n < k or not board_chars.issuperset(word_chars):
            return False

        def backtrack(coord, idx):
            x, y = coord
            if not (0 <= x < m and 0 <= y < n) or board[x][y] != word[idx]:
                return False
            if idx == k - 1:
                return True

            char = board[x][y]
            board[x][y] = "0"
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if backtrack((i, j), idx + 1):
                    return True
            board[x][y] = char
            return False

        return any([backtrack((start_row, start_col), 0) for start_row, start_col in \
            [(i, j) for i in range(m) for j in range(n) if board[i][j] == word[0]]])
