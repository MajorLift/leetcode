# Game of Life
# https://leetcode.com/problems/game-of-life/
# Accepted 2023-04-12 03:05 UTC · Python · 37 ms · 14 MB

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        DIRECTIONS = set(product((1, 0, -1), (1, 0, -1))) - set([(0, 0)])
        for i, j in product(range(m), range(n)):
            live_neighbors = 0
            for direction in DIRECTIONS:
                x, y = map(sum, zip((i, j), direction))
                if 0 <= x < m and 0 <= y < n:
                    live_neighbors += board[x][y] & 1

            if board[i][j] == 1 and 2 <= live_neighbors <= 3 \
                or board[i][j] == 0 and live_neighbors == 3:
                board[i][j] |= 1 << 1

        for i, j in product(range(m), range(n)):
            board[i][j] >>= 1
