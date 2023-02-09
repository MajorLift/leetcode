# Decode Ways
# https://leetcode.com/problems/decode-ways/
# Accepted 2023-02-09 02:41 UTC · Python · 33 ms · 14.2 MB

class Solution:
    def numDecodings(self, s: str) -> int:
        cnt = 0
        @cache
        def dp(idx):
            nonlocal cnt
            if idx < len(s) and s[idx] == "0":
                return 0
            if idx >= len(s) - 1:
                return 1
            cnt += dp(idx + 1) + (dp(idx + 2) if 10 <= int(s[idx:idx + 2]) <= 26 else 0)
            return cnt
        return dp(0)
