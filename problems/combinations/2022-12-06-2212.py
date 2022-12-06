# Combinations
# https://leetcode.com/problems/combinations/
# Accepted 2022-12-06 22:12 UTC · Python · 458 ms · 16 MB

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(start = 1, path = []):
            if len(path) == k:
                output.append(path)
            for num in range(start, n + 1):
                backtrack(num + 1, path + [num])
        backtrack()
        return output
