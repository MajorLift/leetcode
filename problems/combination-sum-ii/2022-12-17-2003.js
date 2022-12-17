// Combination Sum II
// https://leetcode.com/problems/combination-sum-ii/
// Accepted 2022-12-17 20:03 UTC · JavaScript · 82 ms · 44.1 MB

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(nums, target) {
  const output = []
  nums.sort()
  ;(function backtrack(path = [], start = 0, remainder = target) {
    if (remainder === 0) output.push(path.slice())
    for (let i = start; i < nums.length; ++i) {
      if (i > start && nums[i] === nums[i - 1]) continue
      if (remainder - nums[i] >= 0) {
        path.push(nums[i])
        backtrack(path, i + 1, remainder - nums[i])
        path.pop()
      }
    }
  })()
  return output
};
