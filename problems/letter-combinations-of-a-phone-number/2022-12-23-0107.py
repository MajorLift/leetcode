# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted 2022-12-23 01:07 UTC · Python · 64 ms · 13.8 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charmap = {k: [chr(ord('a') + 3 * (k - 2) + i) for i in range(3)] for k in range(2, 7)}
        charmap[7] = [chr(ord('p') + i) for i in range(4)]
        charmap[8] = [chr(ord('t') + i) for i in range(3)]
        charmap[9] = [chr(ord('w') + i) for i in range(4)]
        
        return [''.join(e) for e in itertools.product(*[''.join(charmap[int(digit)]) for digit in digits]) if len(digits)]
