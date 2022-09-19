# Course Schedule
# https://leetcode.com/problems/course-schedule/
# Accepted 2022-09-19 02:04 UTC · Python · 241 ms · 15.5 MB

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]
        for [course, prereq] in prerequisites:
            indegrees[course] += 1
            adj_list[prereq].append(course)
            
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        # output = []
        while queue:
            curr = queue.popleft()
            # output.append(curr)
            for course in adj_list[curr]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        return all([x == 0 for x in indegrees])
