# Merge Triplets to Form Target Triplet
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
# Accepted 2023-03-22 17:02 UTC · Python · 2026 ms · 59.2 MB

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = 0
        for a, b, c in triplets:
            if all(u <= v for u, v in zip((a, b, c), target)):
                x, y, z = max(a, x), max(b, y), max(c, z)
                if [x, y, z] == target:
                    return True
        return False
