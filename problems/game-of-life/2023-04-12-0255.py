# Game of Life
# https://leetcode.com/problems/game-of-life/
# Accepted 2023-04-12 02:55 UTC · Python · 36 ms · 13.9 MB

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        prev = deepcopy(board)
        DIRECTIONS = set(product((1, 0, -1), (1, 0, -1))) - set([(0, 0)])
        for i, j in product(range(m), range(n)):
            live_neighbors = 0
            for direction in DIRECTIONS:
                x, y = map(sum, zip((i, j), direction))
                if 0 <= x < m and 0 <= y < n and prev[x][y] == 1:
                    live_neighbors += 1
            board[i][j] = 0 if prev[i][j] == 1 and not 2 <= live_neighbors <= 3 \
                else 1 if prev[i][j] == 0 and live_neighbors == 3 \
                else board[i][j]
