// Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
// Accepted 2023-09-13 06:24 UTC · JavaScript · 60 ms (72.32%) · 44.3 MB (82.49%)

/**
 * @param {number[]} nums
 * @return {number}
 */
var differenceOfSum = function(nums) {
    const sum = (arr) => arr.reduce((acc, curr) => acc + curr)
    const [elemSum, digitSum] = [nums, nums.map(getDigitSum)].map(sum)
    return elemSum - digitSum
};

function getDigitSum(num) {
    let sum = 0
    while (num > 0) {
        sum += num % 10
        num = Math.floor(num / 10)
    }
    return sum
}
