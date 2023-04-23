# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
# Accepted 2023-04-23 00:45 UTC · Python · 928 ms · 16.4 MB

class Solution:
    def longestStrChain(self, words) -> int:
        length_map = defaultdict(set)
        for word in words:
            length_map[len(word)].add(word)
        
        adj = defaultdict(list)
        indegree = {w: 0 for w in words}
        for i in length_map.keys():
            if i + 1 not in length_map:
                continue
            for shorter, longer in product(length_map[i], length_map[i + 1]):
                print(shorter, longer)
                if self.is_predecessor(shorter, longer):
                    adj[shorter].append(longer)
                    indegree[longer] += 1
        # print(adj, indegree)
        # print([k for k,v in indegree.items() if v == 0])

        @cache
        def dfs(node):
            return 1 + max([dfs(child) for child in adj[node]] or [0])
        return max(dfs(node) for node in [k for k,v in indegree.items() if v == 0])
            
    def is_predecessor(self, shorter, longer):
        if len(shorter) + 1 != len(longer):
            return False
        skips = 0
        i = j = 0
        while j < len(longer):
            if i < len(shorter) and shorter[i] == longer[j]:
                i += 1
                j += 1
            else:
                j += 1
                skips += 1
        return skips == 1
