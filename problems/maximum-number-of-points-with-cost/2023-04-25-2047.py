# Maximum Number of Points with Cost
# https://leetcode.com/problems/maximum-number-of-points-with-cost/
# Accepted 2023-04-25 20:47 UTC · Python · 2117 ms · 47.6 MB

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = map(len, (points, points[0]))
        if m == 1: return max(points[0])
        if n == 1: return sum(row[0] for row in points)
        
        def left(row):
            memo = [row[0]] + [0] * (n - 1)
            for i in range(1, n):
                memo[i] = max(memo[i - 1] - 1, row[i])
            return memo

        def right(row):
            memo = [0] * (n - 1) + [row[-1]]
            for i in range(n - 2, -1, -1):
                memo[i] = max(memo[i + 1] - 1, row[i])
            return memo

        prev = points[0]
        for i in range(1, m):
            l, r, curr = left(prev), right(prev), [0] * n
            for j in range(n):
                curr[j] = points[i][j] + max(l[j], r[j])
            prev = curr[:]
        return max(prev)
