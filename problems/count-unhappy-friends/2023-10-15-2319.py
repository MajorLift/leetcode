# Count Unhappy Friends
# https://leetcode.com/problems/count-unhappy-friends/
# Accepted 2023-10-15 23:19 UTC · Python · 365 ms (31.54%) · 29.9 MB (91.79%)

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        partnerOf = {**{x: y for x, y in pairs}, **{y: x for x, y in pairs}}
        return sum(
            any(x in U.getPreferredOver(v) 
                for u in X.getPreferredOver(y)
                    if (U := Person(preferences[u]), v := partnerOf[u]))
            for x in range(n)
                    if (X := Person(preferences[x]), y := partnerOf[x]))

class Person:
    def __init__(self, preference):
        self.preference = preference
    
    def getPreferredOver(self, this):
        return set(self.preference[:self.preference.index(this)])
