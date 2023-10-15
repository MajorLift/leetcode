# Count Unhappy Friends
# https://leetcode.com/problems/count-unhappy-friends/
# Accepted 2023-10-15 21:25 UTC · Python · 357 ms (47.44%) · 29.9 MB (78.46%)

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairOf = {**{x: y for x, y in pairs}, **{y: x for x, y in pairs}}
        ans = 0
        for x in range(n):
            X, y = Person(preferences[x]), pairOf[x]
            for u in X.getPreferredOver(y):
                U, v = Person(preferences[u]), pairOf[u]
                if x in U.getPreferredOver(v):
                    ans += 1
                    break
        return ans

class Person:
    def __init__(self, preference):
        self.preference = preference
    
    def getPreferredOver(self, this):
        return set(self.preference[:self.preference.index(this)])
