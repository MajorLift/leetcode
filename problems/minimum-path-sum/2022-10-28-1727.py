# Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/
# Accepted 2022-10-28 17:27 UTC · Python · 245 ms · 15.7 MB

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1]) if i < m - 1 and j < n - 1 \
                    else grid[i][j] + dp[i + 1][j] if i < m - 1 and j == n - 1 \
                    else grid[i][j] + dp[i][j + 1] if i == m - 1 and j < n - 1 \
                    else grid[i][j]
        return dp[0][0]        

        # min_sum = +math.inf
        # stack = [(grid[0][0], 0, 0)]
        # visited = set()
        # while stack:
        #     curr_sum, x, y = stack.pop()
        #     if x == m - 1 and y == n - 1:
        #         min_sum = min(min_sum, curr_sum)
        #         visited = set()
        #     for i, j in (x + 1, y), (x, y + 1):
        #         if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
        #             stack.append((curr_sum + grid[i][j], i, j))
        #             visited.add((i, j))
        # return min_sum
