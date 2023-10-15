# Count Unhappy Friends
# https://leetcode.com/problems/count-unhappy-friends/
# Accepted 2023-10-15 20:19 UTC · Python · 410 ms (9.23%) · 35 MB (32.56%)

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        people = {i: Person(e) for i, e in enumerate(preferences)}
        unhappy = set()
        for (x, y), (u, v) in combinations(pairs, 2):
            X, Y, U, V = (people[p] for p in (x, y, u, v))
            if X.prefersThisOverThat(u, y) and U.prefersThisOverThat(x, v):
                unhappy |= set([x, u])
            if X.prefersThisOverThat(v, y) and V.prefersThisOverThat(x, u):
                unhappy |= set([x, v])
            if Y.prefersThisOverThat(u, x) and U.prefersThisOverThat(y, v):
                unhappy |= set([y, u])
            if Y.prefersThisOverThat(v, x) and V.prefersThisOverThat(y, u):
                unhappy |= set([y, v])
        return len(unhappy)
            
class Person:
    def __init__(self, preference):
        self.rank = {e: i for i, e in enumerate(preference)}
    
    def prefersThisOverThat(self, this, that):
        return self.rank[this] < self.rank[that]
