# Max Pair Sum in an Array
# https://leetcode.com/problems/max-pair-sum-in-an-array/
# Accepted 2023-09-08 22:09 UTC · Python · 181 ms · 16.6 MB

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, e in enumerate(nums):
            max_digit = 0
            while e:
                pos = 10 ** int(math.log10(e))
                msd = e // pos
                max_digit = max(max_digit, msd)
                e -= msd * pos
            d[max_digit].append(i)

        return max([-1] + [nums[l] + nums[r] for k in d for l, r in combinations(d[k], 2)])
