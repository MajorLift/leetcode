# Minimum Time to Make Rope Colorful
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# Accepted 2023-08-25 19:31 UTC · Python · 989 ms · 28 MB

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        self.n = len(colors)
        self.costs = neededTime
        self.colors = list(colors)
        self.find_clusters()
        print(self.clusters)
        return sum(self.remove_all_but_max(l, r) for l, r in self.clusters)
        
    def find_clusters(self):
        self.clusters = []
        l = r = 0
        while l < self.n:
            while r < self.n and self.colors[l] == self.colors[r]:
                r += 1
            if r > l + 1:
                self.clusters.append((l, r))
            l = r

    def remove_all_but_max(self, start: int, end: int) -> int:
        print(self.costs[start:end])
        return sum(self.costs[start:end]) - max(self.costs[start:end])
