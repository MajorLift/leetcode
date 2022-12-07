// Task Scheduler
// https://leetcode.com/problems/task-scheduler/
// Accepted 2022-12-07 03:06 UTC · JavaScript · 163 ms · 46.2 MB

/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
  const freqs = tasks.reduce((acc, curr) => {
    acc[curr] = (acc[curr] || 0) + 1
    return acc    
  }, {})
  const maxFreq = Math.max(...Object.values(freqs))
  const numTies = Object.values(freqs)
    .filter((e) => e == maxFreq)
    .length
  return Math.max(tasks.length, (maxFreq - 1) * (n + 1) + numTies)
}
