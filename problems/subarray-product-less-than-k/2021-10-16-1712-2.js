// Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/
// Accepted 2021-10-16 17:12 UTC · JavaScript · 1620 ms · 44.9 MB

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    let [product, counter] = [1, 0];
    let [left, right] = [0, 0];
    while (true) {
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
