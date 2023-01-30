# Number of Ways of Cutting a Pizza
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/
# Accepted 2023-01-30 23:43 UTC · Python · 501 ms · 44.9 MB

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])

        @cache
        def hasApple(coord1, coord2):
            (x1, y1), (x2, y2) = coord1, coord2
            return any(pizza[i][j] == "A" for i in range(x1, x2 + 1) for j in range(y1, y2 + 1))

        @cache
        def dp(r, c, cuts):
            if not hasApple((r, c), (m - 1, n - 1)):
                return 0
            if cuts == 1:
                return 1
            res = 0
            for i in range(r + 1, m):
                if hasApple((r, c), (i - 1, n - 1)):
                    res += dp(i, c, cuts - 1)
            for j in range(c + 1, n):
                if hasApple((r, c), (m - 1, j - 1)):
                    res += dp(r, j, cuts - 1)   
            return res % MOD

        return dp(0, 0, k)
