# Count Pairs of Points With Distance k
# https://leetcode.com/problems/count-pairs-of-points-with-distance-k/
# Accepted 2023-09-16 16:43 UTC · Python · 1577 ms (100%) · 30.9 MB (100%)

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        ans, cnt = 0, Counter()
        for x, y in coordinates:
            for t in range(k + 1):
                ans += cnt[(x ^ t, y ^ (k - t))]
            cnt[(x, y)] += 1
        return ans
