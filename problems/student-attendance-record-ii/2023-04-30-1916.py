# Student Attendance Record II
# https://leetcode.com/problems/student-attendance-record-ii/
# Accepted 2023-04-30 19:16 UTC · Python · 989 ms · 16.3 MB

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(k):
            withA, withoutA = deque([1, 3, 8]), deque([1, 2, 4])
            if k < 3:
                return withA[k]
            for i in range(3, k + 1):
                withoutA.append(sum(withoutA) % MOD)
                withA.append((sum(withA) + withoutA[-1]) % MOD)
                withoutA.popleft()
                withA.popleft()
            return withA[-1]
        
        return dp(n) % MOD
