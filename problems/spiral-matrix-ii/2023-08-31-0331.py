# Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/
# Accepted 2023-08-31 03:31 UTC · Python · 43 ms · 16.3 MB

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dir_idx = 0
        mat = [[None] * n for _ in range(n)]
        i = j = 0
        e = 1
        while e <= n ** 2:
            while 0 <= i < n and 0 <= j < n and mat[i][j] == None:
                mat[i][j] = e
                e += 1
                i, j = map(sum, zip((i, j), DIRS[dir_idx]))
            i, j = map(sum, zip((i, j), map(neg, DIRS[dir_idx])))
            dir_idx = (dir_idx + 1) % 4
            i, j = map(sum, zip((i, j), DIRS[dir_idx]))
        return mat
