# Maximum Length of a Concatenated String with Unique Characters
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# Accepted 2023-08-30 20:29 UTC · Python · 959 ms · 16.4 MB

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        lens = list(map(len, arr))
        max_len = 0
        for k in range(1, n + 1):
            for idxs in combinations(range(n), k):
                unique_chars = set()
                is_all_unique = True
                for idx in idxs:
                    idx_chars = set(arr[idx])
                    if len(idx_chars) < len(arr[idx]) or unique_chars & idx_chars:
                        is_all_unique = False
                        break
                    unique_chars |= idx_chars
                if is_all_unique:
                    max_len = max(max_len, sum(lens[i] for i in idxs))
        return max_len
