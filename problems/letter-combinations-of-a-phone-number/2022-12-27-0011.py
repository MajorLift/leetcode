# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted 2022-12-27 00:11 UTC · Python · 30 ms · 14 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        
        charmap = {k: [chr(ord('a') + 3 * (k - 2) + i) for i in range(3)] for k in range(2, 7)}
        charmap[7] = [chr(ord('p') + i) for i in range(4)]
        charmap[8] = [chr(ord('p') + 4 + i) for i in range(3)]
        charmap[9] = [chr(ord('p') + 7 + i) for i in range(4)]

        output = []
        def backtrack(path = [], idx = 0):
            if idx == n:
                output.append(''.join(path))
                return
            for char in charmap[int(digits[idx])]:
                path.append(char)
                backtrack(path, idx + 1)
                path.pop()
        backtrack()
        return output
