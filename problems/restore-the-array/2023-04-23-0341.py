# Restore The Array
# https://leetcode.com/problems/restore-the-array/
# Accepted 2023-04-23 03:41 UTC · Python · 1426 ms · 171.7 MB

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        @cache
        def dp(start):
            if start == n or s[start] == "0":
                return 0
            cnt = 1
            for i in range(start + 1, n + 1):
                if int(s[start:i]) > k:
                    cnt -= 1
                    break
                cnt += dp(i)
            return cnt % MOD
        return dp(0)
