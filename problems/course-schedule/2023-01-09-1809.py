# Course Schedule
# https://leetcode.com/problems/course-schedule/
# Accepted 2023-01-09 18:09 UTC · Python · 90 ms · 15.4 MB

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for prereq, course in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1
        queue = collections.deque([i for i,e in enumerate(indegrees) if e == 0])
        while queue:
            curr = queue.popleft()
            for course in adj[curr]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        return all([e == 0 for e in indegrees])
