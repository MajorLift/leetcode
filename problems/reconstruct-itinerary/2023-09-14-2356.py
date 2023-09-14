# Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
# Accepted 2023-09-14 23:56 UTC · Python · 79 ms (92.09%) · 16.9 MB (66.48%)

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in tickets:
            heappush(adj[u], v)

        output = deque()
        def dfs(u):
            while adj[u]:
                dfs(heappop(adj[u]))
            output.appendleft(u)
        dfs('JFK')
        return output
