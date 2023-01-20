# Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
# Accepted 2023-01-20 23:44 UTC · Python · 82 ms · 14.6 MB

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(deque)
        for src, dst in tickets:
            adj[src].append(dst)

        output = deque()
        def dfs(src):
            while adj[src]:
                dfs(adj[src].popleft())
            output.appendleft(src)
        dfs("JFK")
        return output
