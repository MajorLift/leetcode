# Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# Accepted 2022-06-10 07:50 UTC · Python · 136 ms · 15.4 MB

# [[1,0],[2,0],[3,1],[3,2]]
# adj_next: [[1, 2], [3], [3], []]
# adj_pre: [[], [0], [0], [1, 2]]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = []
        if not prerequisites:
            return [i for i in range(numCourses)]

        # deserialize input into graph and also store in-degree
        adj_list = [[] for i in range(numCourses)]
        in_degrees = [0] * numCourses
        for [course, prereq] in prerequisites[::-1]:
            adj_list[prereq].append(course)
            in_degrees[course] += 1
        
        # find starting points (0 in-degree) and add to queue
        queue = deque([course for course in range(numCourses) if in_degrees[course] == 0])
        if not queue:
            return []
    
        # bfs
        while len(queue) > 0:
            curr = queue.popleft()
            if curr not in path:
                path.append(curr)
            
            for course in adj_list[curr]:
                in_degrees[course] -= 1        
                if in_degrees[course] == 0:
                    queue.append(course)
            
        if any(e > 0 for e in in_degrees):
            return []

        return path
