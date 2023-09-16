# Remove Letter To Equalize Frequency
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/
# Accepted 2023-09-16 18:33 UTC · Python · 44 ms (25.06%) · 16.2 MB (70.76%)

class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(Counter(word).values())
        return len(cnt) == 2 and (cnt[1] == 1 or cnt[min(cnt) + 1] == 1) \
            or len(cnt) == 1 and (1 in cnt or 1 in cnt.values())
