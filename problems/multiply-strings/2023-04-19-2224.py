# Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# Accepted 2023-04-19 22:24 UTC · Python · 154 ms · 13.9 MB

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n, m = len(num1), len(num2)
        output = deque([0] * (n + m))

        for i, j in product(range(n - 1, -1, -1), range(m - 1, -1, -1)):
            mul = int(num1[i]) * int(num2[j]) + output[i + j + 1]
            output[i + j + 1] = mul % 10
            output[i + j] += mul // 10
        while output[0] == 0:
            output.popleft()
        
        return ''.join(map(str, output))
