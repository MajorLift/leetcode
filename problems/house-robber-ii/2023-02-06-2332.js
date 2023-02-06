// House Robber II
// https://leetcode.com/problems/house-robber-ii/
// Accepted 2023-02-06 23:32 UTC · JavaScript · 70 ms · 42.4 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length <= 3) return Math.max(...nums)
    const memo = Array.from({ length: 2 }, () => new Array(nums.length - 1).fill(0))
    for (const j of [0, 1]) {
        for (let i = nums.length - 2; i >= 0; --i) {
            memo[j][i] = Math.max(nums[i + j] + (memo[j][i + 2] ?? 0), (memo[j][i + 1] ?? 0))
        }
    }
    return Math.max(memo[0][0], memo[1][0])
}
