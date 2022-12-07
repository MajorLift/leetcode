# Task Scheduler
# https://leetcode.com/problems/task-scheduler/
# Accepted 2022-12-07 02:43 UTC · Python · 406 ms · 14.3 MB

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = collections.Counter(tasks)
        maxFreq = max(freqs.values())
        numTies = len([k for k,v in freqs.items() if v == maxFreq])
        return max(len(tasks), (maxFreq - 1) * (n + 1) + numTies)
