# Count Unhappy Friends
# https://leetcode.com/problems/count-unhappy-friends/
# Accepted 2023-10-15 21:31 UTC · Python · 363 ms (34.87%) · 30.1 MB (60%)

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        people = {i: Person(e) for i, e in enumerate(preferences)}
        pairOf = {**{x: y for x, y in pairs}, **{y: x for x, y in pairs}}
        ans = 0
        return sum(
            any(x in people[u].getPreferredOver(pairOf[u])
                for u in people[x].getPreferredOver(pairOf[x]))
            for x in range(n))

class Person:
    def __init__(self, preference):
        self.preference = preference
    
    def getPreferredOver(self, this):
        return set(self.preference[:self.preference.index(this)])
