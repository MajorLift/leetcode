# Points That Intersect With Cars
# https://leetcode.com/problems/points-that-intersect-with-cars/
# Accepted 2023-09-10 02:33 UTC · Python · 87 ms · 16.4 MB

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: x[0])
        merged = [tuple(nums[0])]
        for start, end in nums[1:]:
            start_prev, end_prev = merged[-1]
            if start <= end_prev:
                merged[-1] = min(start_prev, start), max(end_prev, end)
            else:
                merged.append((start, end))
        return sum(end - start + 1 for start, end in merged)
