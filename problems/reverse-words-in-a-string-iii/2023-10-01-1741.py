# Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Accepted 2023-10-01 17:41 UTC · Python · 46 ms (51.33%) · 17.1 MB (42.15%)

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split(' '))
