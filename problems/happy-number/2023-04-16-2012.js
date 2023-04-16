// Happy Number
// https://leetcode.com/problems/happy-number/
// Accepted 2023-04-16 20:12 UTC · JavaScript · 63 ms · 43.5 MB

/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let [slow, fast] = [sumOfSquares(n), sumOfSquares(sumOfSquares(n))]
    while (true) {
        if (fast === 1) return true
        if (slow === fast) return false
        slow = sumOfSquares(slow)
        fast = sumOfSquares(sumOfSquares(fast))
    }
}

function sumOfSquares(n) {
    return (n % 10) ** 2 + (n === 0 ? 0 : sumOfSquares(Math.floor(n / 10)))
}
