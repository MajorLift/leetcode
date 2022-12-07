# Task Scheduler
# https://leetcode.com/problems/task-scheduler/
# Accepted 2022-12-07 06:12 UTC · Python · 391 ms · 14.2 MB

class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
      freqs = collections.Counter(tasks)
      maxFreq = max(freqs.values())
      numMax = len([v for v in freqs.values() if v == maxFreq])
      return max(len(tasks), (maxFreq - 1) * (n + 1) + numMax)
