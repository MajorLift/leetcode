# Word Search
# https://leetcode.com/problems/word-search/
# Accepted 2022-12-21 22:13 UTC · Python · 954 ms · 14 MB

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)

        word_chars, board_chars = set([*word]), set([e for row in board for e in row])
        if m * n < k or not board_chars.issuperset(word_chars):
            return False

        state = copy.deepcopy(board)
        def backtrack(coord, idx):
            x, y = coord
            if idx == k - 1:
                return True

            state[x][y] = "0"
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if not (0 <= i < m and 0 <= j < n) or state[i][j] != word[idx + 1]:
                    continue
                if backtrack((i, j), idx + 1):
                    return True
            state[x][y] = board[x][y]
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack((i, j), 0):
                        return True
        return False
