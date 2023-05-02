# Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/
# Accepted 2023-05-02 17:05 UTC · Python · 169 ms · 21.6 MB

class Solution:

    def __init__(self, w: List[int]):
        self.field = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.field, random.random() * self.field[-1])


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
