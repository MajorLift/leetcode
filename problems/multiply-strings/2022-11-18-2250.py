# Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# Accepted 2022-11-18 22:50 UTC · Python · 218 ms · 14 MB

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        n1 = [int(num) for num in num1[::-1]]
        n2 = [int(num) for num in num2[::-1]]
        n, m = len(n1), len(n2)
        ans = [0] * (n + m)
        for i in range(n):
            for j in range(m):
                pos = i + j
                curr = n1[i] * n2[j] + ans[pos]
                ans[pos] = curr % 10
                ans[pos + 1] += curr // 10
        while ans[-1] == 0:
            ans.pop()
        return "".join([str(num) for num in ans[::-1]])
