// Permutations
// https://leetcode.com/problems/permutations/
// Accepted 2022-12-18 06:39 UTC · JavaScript · 122 ms · 45 MB

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
  const output = []
  ;(function backtrack(start = 0) {
    if (start === nums.length) output.push(nums.slice())
    for (let i = start; i < nums.length; ++i) {
      [nums[start], nums[i]] = [nums[i], nums[start]]
      backtrack(start + 1)
      ;[nums[start], nums[i]] = [nums[i], nums[start]]
    }
  })()
  return output
};
