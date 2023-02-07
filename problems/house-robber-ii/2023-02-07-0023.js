// House Robber II
// https://leetcode.com/problems/house-robber-ii/
// Accepted 2023-02-07 00:23 UTC · JavaScript · 59 ms · 42.3 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
/** nums.slice(0, nums.length - 1), nums.slice(1) */
var rob = function(nums) {
    if (nums.length <= 3) return Math.max(...nums)
    const memo = Array.from({ length: 2 }, () => new Array(nums.length - 1).fill(null))
    for (const j of [0, 1]) {
        for (let i = nums.length - 2; i >= 0; --i) {
            memo[j][i] = Math.max(nums[j + i] + (memo[j][i + 2] ?? 0), (memo[j][i + 1] ?? 0))
        }
    }
    return Math.max(memo[0][0], memo[1][0])


    // function dp(i, j) {
    //     if (i < 0) return 0
    //     if (memo[j][i] !== null) return memo[j][i]
    //     return memo[j][i] = Math.max(nums[j + i] + dp(i - 2, j), dp(i - 1, j))
    // }
    // return Math.max(dp(nums.length - 2, 0), dp(nums.length - 2, 1))
}
