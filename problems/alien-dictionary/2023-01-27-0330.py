# Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/
# Accepted 2023-01-27 03:30 UTC · Python · 62 ms · 14 MB

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        all_chars = set(char for word in words for char in word)
        if len(words) < 2:
            return "".join(all_chars)
        
        adj, indegrees = defaultdict(set), defaultdict(int)
        for l, r in zip(words, words[1:]):
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
        queue = deque([char for char in all_chars if indegrees[char] == 0])
        while queue:
            curr = queue.popleft()
            output.append(curr)
            for v in adj[curr]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)

        return "".join(output) if len(output) == len(all_chars) else ""
