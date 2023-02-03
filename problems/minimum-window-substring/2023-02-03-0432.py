# Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# Accepted 2023-02-03 04:32 UTC · Python · 749 ms · 14.6 MB

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len, min_idx = +math.inf, (-1, -1)

        target_set = set([*t])
        idx_map = {char: i for i, char in enumerate(list(target_set))}
        target = [Counter(t)[char] for char in target_set]
        window = [0] * len(target_set)

        if not t or not s:
            return ""

        l = r = 0
        while r < len(s):
            while r < len(s) and any(window[i] < target[i] for i in range(len(target_set))):
                if s[r] in target_set:
                    window[idx_map[s[r]]] += 1
                r += 1
            
            while all(window[i] >= target[i] for i in range(len(target_set))):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_idx = (l, r)
                
                if s[l] in target_set:
                    window[idx_map[s[l]]] -= 1
                l += 1

        if min_len == +math.inf:
            return ""
        i, j = min_idx
        return s[i:j]
