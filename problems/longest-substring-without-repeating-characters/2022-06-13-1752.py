# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Accepted 2022-06-13 17:52 UTC · Python · 140 ms · 14.1 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        hashmap = {}
        maxlen = 0
        while end < len(s):
            # check whether end in hashmap
            # if not, add s[end++] and update max_len
            if s[end] not in hashmap.keys() or hashmap[s[end]] == 0:
                hashmap[s[end]] = 1
                end += 1
                maxlen = max(maxlen, end - start)
            # else, increment start and update hashmap until hashmap[s[end]] is 0
            else:
                while hashmap[s[end]] > 0:
                    hashmap[s[start]] -= 1
                    start += 1
        return maxlen
