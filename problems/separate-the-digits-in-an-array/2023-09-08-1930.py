# Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/
# Accepted 2023-09-08 19:30 UTC · Python · 76 ms · 16.9 MB

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = deque()
        while nums:
            curr = nums.pop()
            output.appendleft(curr % 10)
            curr //= 10
            if curr:
                nums.append(curr)
        return output
