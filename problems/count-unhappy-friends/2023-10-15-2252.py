# Count Unhappy Friends
# https://leetcode.com/problems/count-unhappy-friends/
# Accepted 2023-10-15 22:52 UTC · Python · 346 ms (69.49%) · 29.9 MB (91.79%)

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        people = {i: Person(e) for i, e in enumerate(preferences)}
        pairOf = {**{x: y for x, y in pairs}, **{y: x for x, y in pairs}}
        return sum(
            any(x in U.getPreferredOver(v) 
                for u in X.getPreferredOver(y)
                    if (U := people[u], v := pairOf[u]))
            for x in range(n)
                    if (X := people[x], y := pairOf[x])
        )

class Person:
    def __init__(self, preference):
        self.preference = preference
    
    def getPreferredOver(self, this):
        return set(self.preference[:self.preference.index(this)])
