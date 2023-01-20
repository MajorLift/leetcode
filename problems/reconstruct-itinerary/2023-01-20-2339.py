# Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
# Accepted 2023-01-20 23:39 UTC · Python · 79 ms · 14.5 MB

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        START = "JFK"
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
            adj[src].sort(reverse=True)

        output = []
        def dfs(src):
            while adj[src]:
                dfs(adj[src].pop())
            output.append(src)
        dfs(START)
        return output[::-1]
