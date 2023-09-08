# Max Pair Sum in an Array
# https://leetcode.com/problems/max-pair-sum-in-an-array/
# Accepted 2023-09-08 22:19 UTC · Python · 170 ms · 16.7 MB

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, e in enumerate(nums):
            max_digit = 0
            while e:
                emax = 10 ** int(math.log10(e))
                msd = e // emax
                e -= msd * emax
                max_digit = max(max_digit, msd)
            d[max_digit].append(i)

        return max([nums[l] + nums[r] for k in d for l, r in combinations(d[k], 2)] or [-1])
