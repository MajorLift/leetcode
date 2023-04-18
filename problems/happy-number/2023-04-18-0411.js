// Happy Number
// https://leetcode.com/problems/happy-number/
// Accepted 2023-04-18 04:11 UTC · JavaScript · 76 ms · 45.5 MB

/**
 * @param {number} n
 * @return {boolean}
 */
function isHappy(n) {
    let [slow, fast] = [sumOfSquares(n), sumOfSquares(sumOfSquares(n))]
    while (true) {
        if (fast === 1) return true
        if (slow === fast) return false
        ;[slow, fast] = [sumOfSquares(slow), sumOfSquares(sumOfSquares(fast))]
    }
}
function sumOfSquares(n) {
    if (n === 0) return 0
    return (n % 10) ** 2 + sumOfSquares(Math.floor(n / 10))
}
