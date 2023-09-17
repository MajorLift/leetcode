# Largest Positive Integer That Exists With Its Negative
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
# Accepted 2023-09-17 16:51 UTC · Python · 116 ms (82.42%) · 16.5 MB (47.57%)

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        positive_set, negative_heap = set(), []
        for num in nums:
            if num > 0:
                positive_set.add(num)
            else:
                heappush(negative_heap, num)
        while negative_heap:
            candidate = heappop(negative_heap)
            if -candidate in positive_set:
                return -candidate
        return -1
