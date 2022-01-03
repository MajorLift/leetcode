// Add Strings
// https://leetcode.com/problems/add-strings/
// Accepted 2022-01-03 19:07 UTC · JavaScript · 88 ms · 40.8 MB

/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    let long = num1.length >= num2.length ? num1 : num2
    let short = num1.length < num2.length ? num1 : num2
    short = "0".repeat(long.length - short.length) + short
    
    let sum = ""
    let carry = 0
    for (let i = long.length - 1; i >= 0; i -= 1) {
        const add = (carry + parseInt(long[i]) + parseInt(short[i])) % 10
        carry = Math.floor((carry + parseInt(long[i]) + parseInt(short[i])) / 10)
        sum = add.toString() + sum
    }
    if (carry > 0) sum = carry.toString() + sum
    return sum
};
