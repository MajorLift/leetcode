// House Robber
// https://leetcode.com/problems/house-robber/
// Accepted 2023-02-04 07:13 UTC · JavaScript · 73 ms · 42.3 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const memo = new Array(nums.length).fill(0)
    for (let i = nums.length - 1; i >= 0; --i) {
        memo[i] = Math.max(nums[i] + (memo[i + 2] ?? 0), (memo[i + 1] ?? 0))
    }
    return memo[0]
}
