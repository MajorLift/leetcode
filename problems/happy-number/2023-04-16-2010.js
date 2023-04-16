// Happy Number
// https://leetcode.com/problems/happy-number/
// Accepted 2023-04-16 20:10 UTC · JavaScript · 60 ms · 44 MB

/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let slow = sumOfSquares(n)
    let fast = sumOfSquares(sumOfSquares(n))
    while (true) {
        if (fast === 1) return true
        if (slow === fast) return false
        slow = sumOfSquares(slow)
        fast = sumOfSquares(sumOfSquares(fast))
    }
}

function sumOfSquares(n) {
    let [last, rest] = [n % 10, Math.floor(n / 10)]
    if (rest === 0) return last ** 2 
    return last ** 2 + sumOfSquares(rest)
}
