# Minimum Deletions to Make Character Frequencies Unique
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# Accepted 2023-09-12 05:29 UTC · Python · 111 ms · 17.2 MB

class Solution:
    def minDeletions(self, s: str) -> int:
        ans, cnt = 0, sorted(Counter(s).values(), reverse=True)
        for i in range(1, len(cnt)):
            while cnt[i] and cnt[i] >= cnt[i - 1]:
                cnt[i] -= 1
                ans += 1
        return ans
