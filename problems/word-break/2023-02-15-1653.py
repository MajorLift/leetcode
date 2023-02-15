# Word Break
# https://leetcode.com/problems/word-break/
# Accepted 2023-02-15 16:53 UTC · Python · 51 ms · 14 MB

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        queue, visited = deque([0]), set()
        while queue:
            start = queue.popleft()
            if start in visited:
                continue
            visited.add(start)
            for end in range(start + 1, n + 1):
                if s[start:end] in wordSet:
                    queue.append(end)
                    if end == n:
                        return True
        return False
