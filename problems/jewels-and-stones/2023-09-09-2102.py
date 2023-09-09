# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# Accepted 2023-09-09 21:02 UTC · Python · 42 ms · 16.3 MB

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len(list(filter(lambda stone: stone in set(jewels), stones)))
