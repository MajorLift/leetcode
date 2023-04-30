# Number of Ways to Build Sturdy Brick Wall
# https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/
# Accepted 2023-04-30 00:33 UTC · Python · 1248 ms · 35.2 MB

class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        MOD = 10 ** 9 + 7
        breaks = set()
        def backtrack(path=[], rem=width):
            if rem == 0: 
                breaks.add(tuple(accumulate(path, func=operator.add))[:-1])
                return
            for brick in bricks:
                if rem - brick >= 0:
                    path.append(brick)
                    backtrack(path, rem - brick)
                    path.pop()
        backtrack()

        adj = defaultdict(set)
        for u, v in combinations_with_replacement(breaks, 2):
            if not set(u) & set(v):
                adj[u].add(v)
                adj[v].add(u)

        @cache
        def dp(wall, curr):
            if wall == height:
                return 1
            return sum([dp(wall + 1, v) for v in adj[curr]]) % MOD
        
        return sum([dp(1, b) for b in breaks]) % MOD
