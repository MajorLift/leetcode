// House Robber
// https://leetcode.com/problems/house-robber/
// Accepted 2023-02-04 07:18 UTC · JavaScript · 66 ms · 42.3 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let [acc, prev] = [0, 0]
    nums.reverse()
    for (const num of nums) {
        [acc, prev] = [Math.max(num + prev, acc), acc]
    }
    return acc
}
