// Permutations II
// https://leetcode.com/problems/permutations-ii/
// Accepted 2022-12-18 07:36 UTC · JavaScript · 130 ms · 45.2 MB

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
  const output = []
  nums.sort()
  ;(function backtrack(path = [], used = new Array(nums.length).fill(false)) {
    if (path.length === nums.length) return output.push(path.slice())
    for (let i = 0; i < nums.length; ++i) {
      if (used[i] || i > 0 && used[i - 1] && nums[i] === nums[i - 1]) continue
      used[i] = true
      path.push(nums[i])
      backtrack(path, used)
      path.pop()
      used[i] = false
    }
  })()
  return output
};
