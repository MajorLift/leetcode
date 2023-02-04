// House Robber
// https://leetcode.com/problems/house-robber/
// Accepted 2023-02-04 07:18 UTC · JavaScript · 60 ms · 42 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let [acc, prev] = [0, 0]
    for (const num of nums) {
        [acc, prev] = [Math.max(num + prev, acc), acc]
    }
    return acc
}
