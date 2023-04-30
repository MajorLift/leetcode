# Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/
# Accepted 2023-04-30 18:03 UTC · Python · 195 ms · 20.3 MB

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.idx = list(range(self.n))

    def reset(self) -> List[int]:
        self.idx = list(range(self.n))
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(self.n):
            rand = random.randint(i, self.n - 1)
            self.idx[i], self.idx[rand] = self.idx[rand], self.idx[i]
        return [self.nums[i] for i in self.idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
