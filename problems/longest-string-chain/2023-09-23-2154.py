# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
# Accepted 2023-09-23 21:54 UTC · Python · 221 ms (41.58%) · 16.8 MB (54.14%)

class Solution:
    def longestStrChain(self, words) -> int:
        length_map = defaultdict(set)
        for word in words:
            length_map[len(word)].add(word)
        
        adj = defaultdict(list)
        indegree = {word: 0 for word in words}
        for i in length_map:
            if i + 1 not in length_map:
                continue
            for pre, post in product(length_map[i], length_map[i + 1]):
                if self.is_predecessor(pre, post):
                    adj[pre].append(post)
                    indegree[post] += 1
        
        queue = deque([k for k, v in indegree.items() if v == 0])
        dist = {word: 0 for word in words}
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                dist[v] = max(dist[v], dist[u] + 1)
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return max(dist.values()) + 1
        
    def is_predecessor(self, pre, post):
        m, n = map(len, (pre, post))
        i = j = 0
        has_skipped = False
        while j < n:
            if i < m and pre[i] == post[j]:
                i += 1
            else:
                if has_skipped: 
                    return False
                has_skipped = True
            j += 1
        return True
