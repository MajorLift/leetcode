# Remove Letter To Equalize Frequency
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/
# Accepted 2023-09-17 18:40 UTC · Python · 37 ms (70.95%) · 16.3 MB (33.02%)

class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(Counter(word).values())
        return len(cnt) == 1 and 1 in (min(cnt), cnt[min(cnt)]) \
            or len(cnt) == 2 and 1 in (cnt[1], cnt[min(cnt) + 1])
