// Smallest Range I
// https://leetcode.com/problems/smallest-range-i/
// Accepted 2023-09-13 20:52 UTC · JavaScript · 62 ms (29.55%) · 43.8 MB (78.64%)

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var smallestRangeI = function(nums, k) {
    return Math.max(0, Math.max(...nums) - Math.min(...nums) - 2 * k)
};
