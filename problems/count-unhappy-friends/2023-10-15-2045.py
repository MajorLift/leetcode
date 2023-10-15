# Count Unhappy Friends
# https://leetcode.com/problems/count-unhappy-friends/
# Accepted 2023-10-15 20:45 UTC · Python · 369 ms (25.38%) · 30 MB (78.46%)

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        people = {i: Person(e) for i, e in enumerate(preferences)}
        pairs_dict = {}
        for x, y in pairs:
            pairs_dict[x] = y
            pairs_dict[y] = x

        ans = 0
        for x in range(n):
            y = pairs_dict[x]
            for u in people[x].getPreferredThan(y):
                v = pairs_dict[u]
                if x in people[u].getPreferredThan(v):
                    ans += 1
                    break
        return ans

class Person:
    def __init__(self, preference):
        self.preference = preference
    
    def getPreferredThan(self, this):
        return set(self.preference[:self.preference.index(this)])
