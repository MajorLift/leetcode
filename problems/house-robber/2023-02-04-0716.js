// House Robber
// https://leetcode.com/problems/house-robber/
// Accepted 2023-02-04 07:16 UTC · JavaScript · 58 ms · 42.4 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    return nums.reduce(([acc, prev], curr) => ([Math.max(curr + prev, acc), acc]), [0, 0])[0]
}
