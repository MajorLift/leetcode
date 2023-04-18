// Happy Number
// https://leetcode.com/problems/happy-number/
// Accepted 2023-04-18 04:07 UTC · JavaScript · 79 ms · 45.5 MB

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
    const [last, rest] = [n % 10, Math.floor(n / 10)]
    return last ** 2 + (n === 0 ? 0 : sumOfSquares(rest))
}
