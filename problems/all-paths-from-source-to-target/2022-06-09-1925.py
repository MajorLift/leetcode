# All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/
# Accepted 2022-06-09 19:25 UTC · Python · 177 ms · 15.7 MB

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []
        stack = [[0]]
        while len(stack) > 0:
            curr = stack.pop()
            peak = curr[-1]
            if peak == len(graph) - 1:
                output.append(curr)
            else:
                for next_vertex in graph[peak]:
                    stack.append([*curr, next_vertex])
                
        return output
