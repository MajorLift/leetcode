# Count Unhappy Friends
# https://leetcode.com/problems/count-unhappy-friends/
# Accepted 2023-10-15 23:21 UTC · Python · 349 ms (62.05%) · 30.1 MB (60%)

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        partnerOf = {**{x: y for x, y in pairs}, **{y: x for x, y in pairs}}
        unhappy = 0
        for x in range(n):
            X, y = Person(preferences[x]), partnerOf[x]
            for u in X.getPreferredOver(y):
                U, v = Person(preferences[u]), partnerOf[u]
                if x in U.getPreferredOver(v):
                    unhappy += 1
                    break
        return unhappy

class Person:
    def __init__(self, preference):
        self.preference = preference
    
    def getPreferredOver(self, this):
        return set(self.preference[:self.preference.index(this)])
