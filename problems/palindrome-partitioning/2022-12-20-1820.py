# Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/
# Accepted 2022-12-20 18:20 UTC · Python · 661 ms · 30.3 MB

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        output = []
        dp = [[False for _ in range(n)] for _ in range(n)]
        def backtrack(tmp = [], start = 0):
            if start == n:
                output.append(tmp)
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    backtrack(tmp + [s[start:end + 1]], end + 1)
        backtrack()
        return output
