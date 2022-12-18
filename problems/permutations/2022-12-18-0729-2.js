// Permutations
// https://leetcode.com/problems/permutations/
// Accepted 2022-12-18 07:29 UTC · JavaScript · 157 ms · 45.4 MB

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
  const output = []
  ;(function backtrack(path = [], used = new Array(nums.length).fill(false)) {
    if (path.length === nums.length) output.push(path.slice())
    for (let i = 0; i < nums.length; ++i) {
      if (!used[i]) {
        used[i] = true
        path.push(nums[i])
        backtrack(path, used)
        path.pop()
        used[i] = false
      }
    }
  })()
  return output
};
