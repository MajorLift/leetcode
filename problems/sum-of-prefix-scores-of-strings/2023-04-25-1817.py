# Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
# Accepted 2023-04-25 18:17 UTC · Python · 6189 ms · 609.1 MB

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        cnt = defaultdict(int)
        for word in words:
            for prefix in self.getPrefixes(word):
                cnt[prefix] += 1
                
        return [sum(cnt[prefix] 
                for prefix in self.getPrefixes(word)) 
            for word in words]

    def getPrefixes(self, s):
        return [s[:i + 1] for i in range(len(s))]
