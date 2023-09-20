# Find the Array Concatenation Value
# https://leetcode.com/problems/find-the-array-concatenation-value/
# Accepted 2023-09-20 05:32 UTC · Python · 63 ms (42.07%) · 16.2 MB (97.52%)

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            if len(nums) > 1:
                first, last = nums.pop(0), nums.pop()
                ans += first * 10 ** int(math.log10(last) + 1) + last
            else:
                ans += nums.pop()                
        return ans
