// Count Primes
// https://leetcode.com/problems/count-primes/
// Accepted 2022-12-15 21:22 UTC · JavaScript · 1523 ms · 176.2 MB

/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    const nums = [false, false]
    if (n > 1) {
        nums.push(...new Array(n - 1).fill(true))
        for (let i = 2; i < Math.floor(Math.sqrt(n)) + 1; ++i) {
            if (!nums[i]) continue
            for (let j = 2; j < Math.floor(n / i) + 1; ++j) {
                nums[i * j] = false
            }
        }
    }
    return nums.reduce((acc, curr) => (curr ? acc + 1 : acc), 0) - Number(nums[nums.length - 1])
};
