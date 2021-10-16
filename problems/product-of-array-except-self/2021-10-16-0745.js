// Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/
// Accepted 2021-10-16 07:45 UTC · JavaScript · 124 ms · 54.8 MB

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const answer = [];
    // const [leftArr, rightArr] = [[], [...nums]];
    const [leftArr, rightArr] = [[], []];
    for (let i = 0; i < nums.length; i += 1) {
        leftArr.push(1);
        rightArr.push(1);
    }
    for (let i = 1; i < nums.length; i += 1) {
        leftArr[i] = leftArr[i - 1] * nums[i - 1];
    }
    for (let j = nums.length - 2; j >= 0; j -= 1) {
        rightArr[j] = rightArr[j + 1] * nums[j + 1];
    }
    for (let k = 0; k < nums.length; k += 1) {
        answer[k] = leftArr[k] * rightArr[k];
    }
    return answer;
};
