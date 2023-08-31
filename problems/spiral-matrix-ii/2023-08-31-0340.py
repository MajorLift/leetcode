# Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/
# Accepted 2023-08-31 03:40 UTC · Python · 44 ms · 16.5 MB

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dir_idx = 0

        def forward(i, j, direction):
            return map(sum, zip((i, j), direction))

        def backward(i, j, direction):
            return map(sum, zip((i, j), map(neg, direction)))

        def turn_right(dir_idx):
            return (dir_idx + 1) % 4

        mat = [[None] * n for _ in range(n)]
        i = j = 0
        e = 1
        while e <= n ** 2:
            while 0 <= i < n and 0 <= j < n and mat[i][j] is None:
                mat[i][j] = e
                e += 1
                i, j = forward(i, j, DIRS[dir_idx])
            i, j = backward(i, j, DIRS[dir_idx])
            dir_idx = turn_right(dir_idx)
            i, j = forward(i, j, DIRS[dir_idx])
        return mat
