// House Robber II
// https://leetcode.com/problems/house-robber-ii/
// Accepted 2023-02-03 18:04 UTC · JavaScript · 70 ms · 42.6 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length <= 3) return Math.max(...nums)
    let global_max = -Infinity
    for (const arr of [nums.slice(0, nums.length - 1), nums.slice(1)]) {
        let [acc, prev] = [0, 0]
        for (const curr of arr) {
            [acc, prev] = [Math.max(curr + prev, acc), acc]
        }
        global_max = Math.max(global_max, acc)
    }
    return global_max
};
