// House Robber
// https://leetcode.com/problems/house-robber/
// Accepted 2023-02-04 07:12 UTC · JavaScript · 64 ms · 42.2 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const memo = new Array(nums.length).fill(0)
    for (let i = 0; i < nums.length; ++i) {
        memo[i] = Math.max(nums[i] + (memo[i - 2] ?? 0), (memo[i - 1] ?? 0))
    }
    return memo[nums.length - 1]
};
