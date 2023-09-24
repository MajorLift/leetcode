# Champagne Tower
# https://leetcode.com/problems/champagne-tower/
# Accepted 2023-09-24 21:14 UTC · Python · 124 ms (26.94%) · 16.3 MB (90.37%)

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = [[0] * k for k in range(1, 102)]
        memo[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                flow = max(0, (memo[i][j] - 1.0) / 2.0)
                memo[i + 1][j] += flow
                memo[i + 1][j + 1] += flow
        return min(1, memo[query_row][query_glass])
