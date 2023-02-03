// House Robber II
// https://leetcode.com/problems/house-robber-ii/
// Accepted 2023-02-03 21:59 UTC · JavaScript · 73 ms · 41.6 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length <= 3) return Math.max(...nums)
    const candidates = [nums.slice(0, nums.length - 1), nums.slice(1)]
    const memo = Array.from({ length: 2 }, () => new Array(nums.length - 1).fill(null))
    function dp(c, i = nums.length - 2) {
        if (i < 0) return 0
        if (memo[c][i] !== null) return memo[c][i]
        return memo[c][i] = Math.max(candidates[c][i] + dp(c, i - 2), dp(c, i - 1))
    }
    return Math.max(dp(0), dp(1))
};
