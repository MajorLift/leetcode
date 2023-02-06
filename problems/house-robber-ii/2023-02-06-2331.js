// House Robber II
// https://leetcode.com/problems/house-robber-ii/
// Accepted 2023-02-06 23:31 UTC · JavaScript · 71 ms · 42 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length <= 3) return Math.max(...nums)
    const memo = Array.from({ length: 2 }, () => new Array(nums.length - 1).fill(0))
    for (const j of [0, 1]) {
        for (let i = 0; i < nums.length - 1; ++i) {
            memo[j][i] = Math.max(nums[i + j] + (memo[j][i - 2] ?? 0), (memo[j][i - 1] ?? 0))
        }
    }
    return Math.max(memo[0][nums.length - 2], memo[1][nums.length - 2])
}
