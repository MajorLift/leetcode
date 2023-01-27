# Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/
# Accepted 2023-01-27 00:20 UTC · Python · 50 ms · 13.9 MB

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""
        if len(words) == 1:
            return "".join(set(words[0]))

        adj = defaultdict(set)
        indegrees = defaultdict(int)
        for l, r in zip(words, words[1:]):
            for char in set([*l] + [*r]):
                if char not in indegrees:
                    indegrees[char] += 0
            for u, v in zip(l, r):
                if u != v:
                    if v not in adj[u]:
                        adj[u].add(v)
                        indegrees[v] += 1
                    break
            else:
                if len(l) > len(r):
                    return ""
        
        output = []
        queue = deque([char for char in indegrees.keys() if indegrees[char] == 0])
        while queue:
            curr = queue.popleft()
            output.append(curr)
            for v in adj[curr]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)

        return "".join(output) if len(output) == len(indegrees.keys()) else ""
