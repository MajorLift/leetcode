# Task Scheduler
# https://leetcode.com/problems/task-scheduler/
# Accepted 2022-12-07 20:26 UTC · Python · 392 ms · 14.4 MB

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = collections.Counter(tasks)
        maxFreq = max(freqs.values())

        pq = [(-freq, task) for task, freq in freqs.items()]
        heapq.heapify(pq)
        heapq.heappop(pq)
        idle = (maxFreq - 1) * n
        while pq:
            freq, _ = heapq.heappop(pq)
            idle -= min(maxFreq - 1, -freq)
        return len(tasks) + (idle if idle > 0 else 0)
