// Count Primes
// https://leetcode.com/problems/count-primes/
// Accepted 2022-12-15 21:25 UTC · JavaScript · 1219 ms · 176.7 MB

/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    const nums = [0, 0]
    if (n > 1) {
        nums.push(...new Array(n - 1).fill(1))
        for (let i = 2; i < Math.floor(Math.sqrt(n)) + 1; ++i) {
            if (!nums[i]) continue
            for (let j = 2; j < Math.floor(n / i) + 1; ++j) {
                nums[i * j] = 0
            }
        }
    }
    return nums.reduce((acc, curr) => acc + curr, 0) - nums[n]
};
