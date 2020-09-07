# Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Accepted 2020-09-07 13:16 UTC · Python · 96 ms · 14 MB

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        odd = False
        if (m+n) % 2 == 1:
            odd = True
        limit = int((m+n) // 2)
            
        merged = []
        
        i = 0
        j = 0
        idx = 0
        while idx <= limit:
            if i >= m and j >= n:
                break
            elif i >= m:
                while j < n:
                    merged.append(nums2[j])
                    j += 1
                    idx += 1
            elif j >= n:
                while i < m:
                    merged.append(nums1[i])
                    i += 1
                    idx += 1
            else:
                if nums1[i] <= nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
                idx += 1
        
        if odd:
            return float(merged[limit])
        else:
            return (merged[limit] + merged[limit-1]) / 2
