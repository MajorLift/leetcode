// House Robber
// https://leetcode.com/problems/house-robber/
// Accepted 2023-02-04 07:00 UTC · JavaScript · 72 ms · 41.3 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length <= 2) return Math.max(...nums)
    const memo = new Array(nums.length).fill(null)
    return (function dp(i = 0) {
        if (i >= nums.length) return 0
        if (memo[i] !== null) return memo[i]
        return memo[i] = Math.max(nums[i] + dp(i + 2), dp(i + 1))
    })()
};
