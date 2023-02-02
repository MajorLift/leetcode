# Happy Number
# https://leetcode.com/problems/happy-number/
# Accepted 2023-02-02 07:51 UTC · Python · 32 ms · 13.8 MB

class Solution:
    def isHappy(self, n: int) -> bool:
        num, numset = n, set()
        while True:
            num = sum(int(d) ** 2 for d in str(num))
            if num == 1:
                return True
            if num in numset:
                return False
            numset.add(num)
