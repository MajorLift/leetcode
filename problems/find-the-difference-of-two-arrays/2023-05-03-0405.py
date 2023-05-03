# Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Accepted 2023-05-03 04:05 UTC · Python · 172 ms · 16.7 MB

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = map(set, (nums1, nums2))
        return [set1 - set2, set2 - set1]
