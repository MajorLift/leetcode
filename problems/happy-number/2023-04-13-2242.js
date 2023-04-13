// Happy Number
// https://leetcode.com/problems/happy-number/
// Accepted 2023-04-13 22:42 UTC · JavaScript · 62 ms · 44.2 MB

/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let slow = fast = n
    do {
        slow = sumOfSquares(slow)
        fast = sumOfSquares(sumOfSquares(fast))
    } while (slow !== fast)
    if (fast === 1) return true
    return false
}

function sumOfSquares(n) {
    let [last, rest] = [n % 10, Math.floor(n / 10)]
    if (rest === 0) return last ** 2 
    return last ** 2 + sumOfSquares(rest)
}
