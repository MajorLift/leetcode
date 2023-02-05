# Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
# Accepted 2023-02-05 22:52 UTC · Python · 511 ms · 15.5 MB

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(max(piles) + 1), True, lo=1, 
            key=lambda k: sum([math.ceil(piles[i] / k) for i in range(len(piles))]) <= h)
