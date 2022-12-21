# Word Search
# https://leetcode.com/problems/word-search/
# Accepted 2022-12-21 22:46 UTC · Python · 1150 ms · 13.9 MB

from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)

        word_cnt, board_cnt = Counter([*word]), Counter([e for row in board for e in row])
        if m * n < k or not all([word_cnt[k] <= board_cnt.get(k, -math.inf) for k in word_cnt]):
            return False

        visited = set()
        def backtrack(curr, idx):
            if idx == k - 1:
                return True
            x, y = curr
            visited.add(curr)
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[idx + 1] or (i, j) in visited:
                    continue
                if backtrack((i, j), idx + 1):
                    return True
            visited.remove(curr)
            return False

        return any([backtrack((start_row, start_col), 0) for start_row, start_col in \
            [(i, j) for i in range(m) for j in range(n) if board[i][j] == word[0]]])
