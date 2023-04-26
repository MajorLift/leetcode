# Shortest Subarray with Sum at Least K
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# Accepted 2023-04-26 03:22 UTC · Python · 1253 ms · 30.6 MB

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        psums = [0] + list(accumulate(nums, operator.add))
        monoq = deque()
        ans = +inf
        for r in range(n + 1):
            while monoq and psums[r] <= psums[monoq[-1]]:
                monoq.pop()
            while monoq and psums[r] - psums[monoq[0]] >= k:
                ans = min(ans, r - monoq.popleft())
            monoq.append(r)
        return ans if ans < +inf else -1
