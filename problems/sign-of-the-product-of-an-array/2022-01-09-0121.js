// Sign of the Product of an Array
// https://leetcode.com/problems/sign-of-the-product-of-an-array/
// Accepted 2022-01-09 01:21 UTC · JavaScript · 68 ms · 40 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    return nums.reduce((acc, curr) => (curr > 0 ? acc : curr < 0 ? -1 * acc : 0), +1)
};
