# Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# Accepted 2023-02-03 06:51 UTC · Python · 966 ms · 14.7 MB

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or any(Counter(s)[k] < Counter(t)[k] for k in set(t)):
            return ""
        min_len, min_idx = +math.inf, (-1, -1)
        target = Counter(t)
        window = {char: 0 for char in target}

        l = r = 0
        while r < len(s):
            while r < len(s) and any(window[k] < target[k] for k in target):
                if s[r] in target:
                    window[s[r]] += 1
                r += 1
            
            while all(window[k] >= target[k] for k in target):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_idx = (l, r)
                
                if s[l] in target:
                    window[s[l]] -= 1
                l += 1

        if min_len == +math.inf:
            return ""
        i, j = min_idx
        return s[i:j]
