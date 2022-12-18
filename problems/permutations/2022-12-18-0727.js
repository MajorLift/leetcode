// Permutations
// https://leetcode.com/problems/permutations/
// Accepted 2022-12-18 07:27 UTC · JavaScript · 106 ms · 45.1 MB

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
  const output = []
  ;(function backtrack(path = [], used = new Array(nums.length).fill(false)) {
    if (path.length === nums.length) {
      output.push(path.slice())
      return
    }
    for (let i = 0; i < nums.length; ++i) {
      if (!used[i]) {
        used.splice(i, 1, true)
        path.push(nums[i])
        backtrack(path, used)
        path.pop()
        used.splice(i, 1, false)
      }
    }
  })()
  return output
};
