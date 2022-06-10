# Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# Accepted 2022-06-10 07:55 UTC · Python · 204 ms · 15.3 MB

# [[1,0],[2,0],[3,1],[3,2]]
# adj_next: [[1, 2], [3], [3], []]
# adj_pre: [[], [0], [0], [1, 2]]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = []
        if not prerequisites:
            return [i for i in range(numCourses)]

        # deserialize input into graph and also store in-degrees
        adj_list = [[] for i in range(numCourses)]
        in_degrees = [0] * numCourses
        for [course, prereq] in prerequisites:
            adj_list[prereq].append(course)
            in_degrees[course] += 1
        
        # find starting points (0 in-degree) and add to queue
        queue = deque([course for course in range(numCourses) if in_degrees[course] == 0])
        if not queue:
            return []
    
        # bfs. decrement in-degree of all adjacent vertices of current vertex, 
        # and add vertices with 0 in-degree to queue
        while len(queue) > 0:
            curr = queue.popleft()
            if curr not in path:
                path.append(curr)
            
            for course in adj_list[curr]:
                in_degrees[course] -= 1        
                if in_degrees[course] == 0:
                    queue.append(course)
        
        # if any vertex still has a non-zero in-degree, the graph is cyclic or disconnected
        if any(e > 0 for e in in_degrees):
            return []

        return path
