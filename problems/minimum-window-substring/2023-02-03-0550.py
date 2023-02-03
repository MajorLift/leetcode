# Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# Accepted 2023-02-03 05:50 UTC · Python · 847 ms · 14.7 MB

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        min_len, min_idx = +math.inf, (-1, -1)
        window, target = defaultdict(int), Counter(t)

        def compare_dict(d1, d2):
            if len(d1) == len(d2):
                if d1 == d2: 
                    return 0
                return -1 if any(d1[k] < d2[k] for k in d1) else +1
            return -1 if len(d1) < len(d2) else +1

        l = r = 0
        while r < len(s):
            while r < len(s) and compare_dict(window, target) < 0:
                if s[r] in target:
                    window[s[r]] += 1
                r += 1
            
            while compare_dict(window, target) >= 0:
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
