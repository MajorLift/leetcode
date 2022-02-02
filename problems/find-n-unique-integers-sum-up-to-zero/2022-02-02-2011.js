// Find N Unique Integers Sum up to Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
// Accepted 2022-02-02 20:11 UTC · JavaScript · 96 ms · 43 MB

/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    const output = n % 2 === 0 ? [] : [0];
    for (let i = 1; i <= Math.floor(n / 2); i++) {
        output.push(-i, i);
    }
    return output;
};
