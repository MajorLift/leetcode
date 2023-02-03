// House Robber II
// https://leetcode.com/problems/house-robber-ii/
// Accepted 2023-02-03 18:02 UTC · JavaScript · 60 ms · 42.1 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length <= 3) return Math.max(...nums)
    return Math.max(...[nums.slice(0, nums.length - 1), nums.slice(1)]
        .map((arr) => (arr.reduce(([acc, prev], curr) => 
            ([Math.max(curr + prev, acc), acc]), [0, 0])[0])))
};
