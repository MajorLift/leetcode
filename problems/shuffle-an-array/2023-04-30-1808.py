# Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/
# Accepted 2023-04-30 18:08 UTC · Python · 193 ms · 20.3 MB

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        idx = list(range(self.n))
        for i in range(self.n):
            rand = random.randint(i, self.n - 1)
            idx[i], idx[rand] = idx[rand], idx[i]
        return [self.nums[i] for i in idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
