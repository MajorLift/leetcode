# Word Search
# https://leetcode.com/problems/word-search/
# Accepted 2022-12-21 22:41 UTC · Python · 6512 ms · 14 MB

from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)

        word_cnt, board_cnt = Counter([*word]), Counter([e for row in board for e in row])
        if m * n < k or not all([k in board_cnt and word_cnt[k] <= board_cnt[k]] for k in word_cnt.keys()):
            return False

        def backtrack(curr, idx):
            if idx == k - 1:
                return True
            x, y = curr
            char = board[x][y]
            board[x][y] = "0"
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[idx + 1]:
                    continue
                if backtrack((i, j), idx + 1):
                    return True
            board[x][y] = char
            return False

        return any([backtrack((start_row, start_col), 0) for start_row, start_col in \
            [(i, j) for i in range(m) for j in range(n) if board[i][j] == word[0]]])
