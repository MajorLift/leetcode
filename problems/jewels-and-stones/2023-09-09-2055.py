# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# Accepted 2023-09-09 20:55 UTC · Python · 34 ms · 16.3 MB

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in (_ := set(jewels)) for stone in stones)
