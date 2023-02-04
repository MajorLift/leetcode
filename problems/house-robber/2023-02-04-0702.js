// House Robber
// https://leetcode.com/problems/house-robber/
// Accepted 2023-02-04 07:02 UTC · JavaScript · 78 ms · 41.4 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const memo = new Array(nums.length).fill(null)
    return (function dp(i = nums.length - 1) {
        if (i < 0) return 0
        if (memo[i] !== null) return memo[i]
        return memo[i] = Math.max(nums[i] + dp(i - 2), dp(i - 1))
    })()
};
