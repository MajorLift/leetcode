// Permutations
// https://leetcode.com/problems/permutations/
// Accepted 2022-12-18 07:26 UTC · JavaScript · 71 ms · 45.7 MB

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
        path.push(nums[i])
        backtrack(path, [...used.slice(0, i), true, ...used.slice(i + 1)])
        path.pop()
      }
    }
  })()
  return output
};
