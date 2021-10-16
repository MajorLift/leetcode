// Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/
// Accepted 2021-10-16 17:11 UTC · JavaScript · 1868 ms · 44.8 MB

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    let [product, counter] = [1, 0];
    for (let [left, right] = [0, 0]; left <= right;) {
        product *= nums[right];
        if (product < k) {
            counter++;
            if (right < nums.length - 1) right++;
            else {
                product = 1;
                right = ++left;
            }
        }
        else {
            product = 1;
            if (left < nums.length - 1) right = ++left;
            else break;
        }
    }
    return counter;
};
