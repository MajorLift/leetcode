# Find the Array Concatenation Value
# https://leetcode.com/problems/find-the-array-concatenation-value/
# Accepted 2023-09-20 05:31 UTC · Python · 64 ms (37.24%) · 16.3 MB (84.55%)

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            if len(nums) > 1:
                first, last = nums.pop(0), nums.pop()
                first *= 10 ** (math.floor(math.log10(last)) + 1)
                first += last
                ans += first
            else:
                ans += nums.pop()                
        return ans
