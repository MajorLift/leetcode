# Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
# Accepted 2023-01-20 23:42 UTC · Python · 85 ms · 14.7 MB

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)
        for src, dst in sorted(tickets):
            adj[src].append(dst)

        output = deque()
        def dfs(src):
            while adj[src]:
                dfs(adj[src].popleft())
            output.appendleft(src)
        dfs("JFK")
        return output
