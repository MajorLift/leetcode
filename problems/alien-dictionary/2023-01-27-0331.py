# Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/
# Accepted 2023-01-27 03:31 UTC · Python · 59 ms · 14 MB

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        all_chars = set(char for word in words for char in word)
        if len(words) < 2:
            return "".join(all_chars)
        
        adj = defaultdict(set)
        for l, r in zip(words, words[1:]):
            for u, v in zip(l, r):
                if u != v:
                    if v not in adj[u]:
                        adj[u].add(v)
                    break
            else:
                if len(l) > len(r):
                    return ""
        
        is_cycle = dict()
        output = []
        def dfs(node):
            '''
            Returns False if input node is part of a cycle.
            Mutates output list by appending acyclic nodes.
            '''
            if node in is_cycle:
                return is_cycle[node]
            is_cycle[node] = False
            for v in adj[node]:
                if not dfs(v):
                    return False
            is_cycle[node] = True
            output.append(node)
            return True

        return "".join(output[::-1]) \
            if all(dfs(char) for char in all_chars) else ""
