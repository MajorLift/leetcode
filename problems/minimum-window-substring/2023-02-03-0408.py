# Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# Accepted 2023-02-03 04:08 UTC · Python · 1454 ms · 14.8 MB

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        min_len, min_idx = +math.inf, (-1, -1)
        target = Counter(t)
        window = defaultdict(int)

        def compare(d1, d2):
            if len(d1) < len(d2):
                return -1
            if len(d1) > len(d2):
                return +1
            if len(d1) == len(d2):
                if d1 == d2:
                    return 0
                if any(d1[k] < d2[k] for k in d1):
                    return -1
                if all(d1[k] >= d2[k] for k in d1):
                    return +1
            return 0

        if not t or not s or compare({k: Counter(s)[k] for k in target}, target) < 0:
            return ""

        l = r = 0
        while r < n:
            while r < n and compare(window, target) < 0:
                if s[r] in target:
                    window[s[r]] += 1
                r += 1
            
            while compare(window, target) >= 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_idx = (l, r)
                
                if s[l] in target:
                    window[s[l]] -= 1
                    if window[s[l]] <= 0:
                        del window[s[l]]
                l += 1

        if min_len < +math.inf:
            i, j = min_idx
            return s[i:j]
        return ""
