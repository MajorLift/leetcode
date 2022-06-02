# Permutations II
# https://leetcode.com/problems/permutations-ii/
# Accepted 2022-06-02 05:07 UTC · Python · 86 ms · 14.4 MB

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        def backtrack(first = 0):
            if first == n:
                output.append(nums[:])
            else:
                lookup = set()
                for i in range(first, n):
                    if nums[i] not in lookup:
                        nums[first], nums[i] = nums[i], nums[first]
                        backtrack(first + 1)
                        nums[first], nums[i] = nums[i], nums[first]
                        lookup.add(nums[i])
                    
        backtrack()
        return output
