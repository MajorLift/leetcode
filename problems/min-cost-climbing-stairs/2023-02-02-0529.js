// Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/
// Accepted 2023-02-02 05:29 UTC · JavaScript · 70 ms · 44.3 MB

/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (cost) { 
  return Math.min(...cost.reduce(([acc, prev], curr) => ([Math.min(acc, prev) + curr, acc]), [0, 0]))
}
