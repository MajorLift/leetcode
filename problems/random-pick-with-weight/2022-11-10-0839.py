# Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/
# Accepted 2022-11-10 08:39 UTC · Python · 389 ms · 19.2 MB

class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sum = [self.w[0]]
        for weight in self.w[1:]:
            self.prefix_sum.append(self.prefix_sum[-1] + weight)
        self.sum = self.prefix_sum[-1]

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.prefix_sum, random.random() * self.sum)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
