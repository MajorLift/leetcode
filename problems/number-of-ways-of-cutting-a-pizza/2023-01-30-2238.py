# Number of Ways of Cutting a Pizza
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/
# Accepted 2023-01-30 22:38 UTC · Python · 182 ms · 15.9 MB

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])
        suffixSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                suffixSum[i][j] = int(pizza[i][j] == "A") + suffixSum[i + 1][j] + suffixSum[i][j + 1] - suffixSum[i + 1][j + 1]

        @cache
        def dp(r, c, cuts):
            if suffixSum[r][c] == 0: return 0
            if cuts == 0: return 1
            res = 0
            for i in range(r + 1, m):
                if suffixSum[r][c] > suffixSum[i][c]:
                    res += dp(i, c, cuts - 1)
            for j in range(c + 1, n):
                if suffixSum[r][c] > suffixSum[r][j]:
                    res += dp(r, j, cuts - 1)   
            return res % MOD

        return dp(0, 0, k - 1)
