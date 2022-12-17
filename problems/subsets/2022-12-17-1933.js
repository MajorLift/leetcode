// Subsets
// https://leetcode.com/problems/subsets/
// Accepted 2022-12-17 19:33 UTC · JavaScript · 111 ms · 44.3 MB

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
  const output = []
  ;(function backtrack(path, start) {
    output.push(path.slice())
    for (let i = start; i < nums.length; ++i) {
      path.push(nums[i])
      backtrack(path, i + 1)
      path.pop()
    }
  })([], 0)
  return output
};
