// Combination Sum
// https://leetcode.com/problems/combination-sum/
// Accepted 2022-12-17 20:00 UTC · JavaScript · 116 ms · 45.7 MB

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(nums, target) {
  const output = []
  ;(function backtrack(path = [], start = 0, remainder = target) {
    if (remainder === 0) output.push(path.slice())
    for (let i = start; i < nums.length; ++i) {
      if (remainder - nums[i] >= 0) {
        path.push(nums[i])
        backtrack(path, i, remainder - nums[i])
        path.pop()
      }
    }
  })()
  return output
};
