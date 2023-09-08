# Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Accepted 2023-09-08 16:39 UTC · Python · 44 ms · 16.3 MB

class Solution:
    def countDigits(self, num: int) -> int:
        cnt = Counter(str(num))
        ans = 0
        for digit in cnt:
            if not num % int(digit):
                ans += cnt[digit]
        return ans
