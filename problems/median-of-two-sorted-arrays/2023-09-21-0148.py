# Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Accepted 2023-09-21 01:48 UTC · Python · 94 ms (43.43%) · 16.4 MB (91.51%)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = map(len, (nums1, nums2))
        i = j = 0
        merged = []
        while True:
            if i == m and j == n:
                break
            elif i == m:
                while j < n:
                    merged.append(nums2[j])
                    j += 1
            elif j == n:
                while i < m:
                    merged.append(nums1[i])
                    i += 1
            elif nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        return ((merged[(m + n) // 2 - 1] + merged[(m + n) // 2]) / 2, 
                merged[(m + n) // 2]
            )[(m + n) % 2]
